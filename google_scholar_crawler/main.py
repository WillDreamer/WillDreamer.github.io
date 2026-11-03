"""Fetch a complete Scholar profile before replacing the published data."""

import argparse
from datetime import datetime, timezone
import json
import logging
import os
from pathlib import Path
import re
import subprocess
import sys


def fetch_author(scholar_id):
    from scholarly import scholarly

    scholarly.set_logger(True)
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    return author


def validate_author(author, scholar_id):
    if not isinstance(author, dict) or author.get('scholar_id') != scholar_id:
        raise ValueError('Scholar returned a different or missing profile ID')
    if not isinstance(author.get('name'), str) or not author['name'].strip():
        raise ValueError('Scholar returned an empty author name')
    if type(author.get('citedby')) is not int or author['citedby'] < 0:
        raise ValueError('Scholar returned an invalid citation count')
    publications = author.get('publications')
    if not isinstance(publications, list) or not publications:
        raise ValueError('Scholar returned an incomplete publications list')
    normalized = {}
    for publication in publications:
        if not isinstance(publication, dict):
            raise ValueError('Scholar returned an invalid publication')
        pub_id = publication.get('author_pub_id')
        if not isinstance(pub_id, str) or not pub_id.startswith(scholar_id + ':'):
            raise ValueError('Scholar returned an invalid publication ID')
        if pub_id in normalized:
            raise ValueError('Scholar returned a duplicate publication')
        if type(publication.get('num_citations')) is not int or publication['num_citations'] < 0:
            raise ValueError('Scholar returned an invalid publication citation count')
        normalized[pub_id] = publication
    return {**author, 'publications': normalized,
            'updated': datetime.now(timezone.utc).isoformat()}


def fetch_with_timeout(scholar_id, timeout):
    # scholarly 1.5.1 can retry HTTP 403 forever. A separate process makes the
    # deadline effective even while that dependency is sleeping or retrying.
    result = subprocess.run(
        [sys.executable, str(Path(__file__).resolve()), '--fetch'],
        env={**os.environ, 'GOOGLE_SCHOLAR_ID': scholar_id},
        stdout=subprocess.PIPE, text=True, check=True, timeout=timeout,
    )
    return json.loads(result.stdout)


def update_results(scholar_id, timeout=180, output_dir=Path('results')):
    author = validate_author(fetch_with_timeout(scholar_id, timeout), scholar_id)
    badge = {'schemaVersion': 1, 'label': 'citations', 'message': str(author['citedby'])}
    output_dir.mkdir(parents=True, exist_ok=True)
    # Nothing is written until the entire fetch and validation have succeeded.
    for filename, data in [('gs_data.json', author), ('gs_data_shieldsio.json', badge)]:
        temporary = output_dir / (filename + '.tmp')
        temporary.write_text(json.dumps(data, ensure_ascii=False) + '\n', encoding='utf-8')
        temporary.replace(output_dir / filename)
    logging.info('Updated %s: %s citations, %s publications',
                 author['name'], author['citedby'], len(author['publications']))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--timeout', type=int, default=180, help='Maximum fetch duration in seconds')
    parser.add_argument('--fetch', action='store_true', help=argparse.SUPPRESS)
    args = parser.parse_args()
    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip()
    if not re.fullmatch(r'[A-Za-z0-9_-]+', scholar_id):
        parser.error('GOOGLE_SCHOLAR_ID must be configured with a valid profile ID')
    if args.timeout <= 0:
        parser.error('--timeout must be positive')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    if args.fetch:
        json.dump(fetch_author(scholar_id), sys.stdout, ensure_ascii=False)
        return 0
    try:
        update_results(scholar_id, args.timeout)
    except subprocess.TimeoutExpired:
        logging.error('Scholar did not complete within %s seconds; keeping previous data. '
                      'Check the request logs for HTTP 403 or rate limiting.', args.timeout)
        return 1
    except (subprocess.CalledProcessError, ValueError, OSError) as error:
        logging.error('Citation update failed; data will not be published: %s', error)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
