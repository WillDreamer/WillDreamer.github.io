import copy
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import main


class CitationUpdateTests(unittest.TestCase):
    scholar_id = 'RGZUJOkAAAAJ'

    def setUp(self):
        self.author = {
            'scholar_id': self.scholar_id, 'name': 'Haixin Wang', 'citedby': 1838,
            'publications': [{'author_pub_id': self.scholar_id + ':paper', 'num_citations': 12}],
        }
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.results = Path(self.directory.name) / 'results'
        self.results.mkdir()
        self.previous = {'gs_data.json': '{"previous": true}\n',
                         'gs_data_shieldsio.json': '{"message": "1701"}\n'}
        for filename, contents in self.previous.items():
            (self.results / filename).write_text(contents, encoding='utf-8')

    def assert_previous_preserved(self):
        for filename, contents in self.previous.items():
            self.assertEqual((self.results / filename).read_text(encoding='utf-8'), contents)

    def test_valid_fetch_updates_both_files(self):
        with patch.object(main, 'fetch_with_timeout', return_value=self.author):
            main.update_results(self.scholar_id, output_dir=self.results)
        author = json.loads((self.results / 'gs_data.json').read_text())
        badge = json.loads((self.results / 'gs_data_shieldsio.json').read_text())
        self.assertEqual(author['citedby'], 1838)
        self.assertEqual(list(author['publications']), [self.scholar_id + ':paper'])
        self.assertTrue(author['updated'].endswith('+00:00'))
        self.assertEqual(badge, {'schemaVersion': 1, 'label': 'citations', 'message': '1838'})

    def test_invalid_responses_preserve_previous_data(self):
        invalid = [None, {}, {**self.author, 'scholar_id': 'wrong'},
                   {**self.author, 'name': ''}, {**self.author, 'publications': []}]
        invalid.extend({**self.author, 'citedby': value} for value in [None, -1, True, '1838'])
        for response in invalid:
            with self.subTest(response=response):
                with patch.object(main, 'fetch_with_timeout', return_value=response):
                    with self.assertRaises(ValueError):
                        main.update_results(self.scholar_id, output_dir=self.results)
                self.assert_previous_preserved()

    def test_invalid_publications_are_rejected(self):
        for publication in [None, {}, {'author_pub_id': 'wrong:paper', 'num_citations': 1},
                            {'author_pub_id': self.scholar_id + ':paper', 'num_citations': -1}]:
            with self.subTest(publication=publication):
                with self.assertRaises(ValueError):
                    main.validate_author({**self.author, 'publications': [publication]}, self.scholar_id)
        duplicate = copy.deepcopy(self.author)
        duplicate['publications'] *= 2
        with self.assertRaises(ValueError):
            main.validate_author(duplicate, self.scholar_id)

    def test_network_failure_preserves_previous_data(self):
        with patch.object(main, 'fetch_with_timeout', side_effect=subprocess.CalledProcessError(1, 'worker')):
            with self.assertRaises(subprocess.CalledProcessError):
                main.update_results(self.scholar_id, output_dir=self.results)
        self.assert_previous_preserved()

    def test_hung_worker_is_killed_and_previous_data_preserved(self):
        worker = Path(self.directory.name) / 'hung_worker.py'
        worker.write_text('import time\ntime.sleep(60)\n', encoding='utf-8')
        with patch.object(main, '__file__', str(worker)):
            with self.assertRaises(subprocess.TimeoutExpired):
                main.update_results(self.scholar_id, timeout=0.1, output_dir=self.results)
        self.assert_previous_preserved()


if __name__ == '__main__':
    unittest.main()
