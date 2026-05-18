---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hello 👋, I am Haixin Wang (汪海昕). I am a second-year Ph.D. student in Computer Science at UCLA, advised by Prof. <a href="https://web.cs.ucla.edu/~yzsun/">Yizhou Sun</a> and collaborating closely with Prof. <a href="https://web.cs.ucla.edu/~weiwang/">Wei Wang</a>. I received the M.S. degree from Peking University. My main research interests include LLM Post-training, Agentic Systems, and Multimodal Learning. I have published several papers at the top international AI Conferences/Journals with total <a href='https://scholar.google.com/citations?user=RGZUJOkAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=google citations"></a>. If you are interested in collaboration, feel free to email me at whx@cs.ucla.edu.

# 📖 Research Interests:
- LLM Post-training
  - Agentic RL
  - Agentic RL Infra
- Agentic System
  - Agent Harness
  - Multi-agent Scaling


# 🔥 News
- *2026.05*: &nbsp;🎉🎉 One paper has been accepted by KDD 2026.
- *2026.04*: &nbsp;🎉🎉 Two papers (One Spotlight) have been accepted by ICML 2026.
- *2025.09*: &nbsp;🎉🎉 Five papers have been accepted by NeurIPS 2025.
- *2025.01*: &nbsp;🎉🎉 One paper has been accepted as oral by AAAI 2025.
- *2024.09*: &nbsp;🎉🎉 I joined the [UCLA DATA MINING LAB](https://ucla-dm.github.io/DM_website/index.html) as a PhD student.


# 💼 Internships &amp; Visiting Scholar
- *2026.03 - Present*, Student researcher intern, Microsoft CoreAI. 
- *2025.06 - 2025.11*, Applied scientist intern, Amazon. 
- *2023.09 - 2024.10*, Visiting scholar, Westlake University.
- *2023.12 - 2024.03*, AI4Science research intern, Microsoft Research Asia.


# 🔖 Selected Publications (* equal contribution, † corresponding author)
- [**T<sup>2</sup>PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning**](https://arxiv.org/abs/2605.02178). **Haixin Wang**, Hejie Cui, Chenwei Zhang, Xin Liu, Shuowei Jin, Shijie Geng, Xinyang Zhang, Nasser Zalmout, Zhenyu Shi, and Yizhou Sun. <img src="https://img.shields.io/badge/ICML%202026-Spotlight-f59e0b?style=flat-square" />  [![](https://img.shields.io/github/stars/WillDreamer/T2PO?style=social&label=Code+Stars)](https://github.com/WillDreamer/T2PO)

- [**ARLArena: A Unified Framework for Stable Agentic Reinforcement Learning**](https://arxiv.org/abs/2602.21534). Xiaoxuan Wang\*, Han Zhang\*, **Haixin Wang\***, Yidan Shi, Ruoyan Li, Kaiqiao Han, Chenyi Tong, Haoran Deng, Renliang Sun, Alexander Taylor, Yanqiao Zhu, Jason Cong, Yizhou Sun, Wei Wang. <img src="https://img.shields.io/badge/ICML%202026-Conference-2563eb?style=flat-square" /> [![](https://img.shields.io/github/stars/WillDreamer/ARL-Arena?style=social&label=Code+Stars)](https://github.com/WillDreamer/ARL-Arena)

- [**FD-Bench: A Modular and Fair Benchmark for Data-driven Fluid Simulation**](https://arxiv.org/abs/2505.20349). Haixin Wang, Ruoyan Li, Fred Xu, Fang Sun, Kaiqiao Han, Zijie Huang, Ching Chang, Xiao Luo, Wei Wang, Yizhou Sun. <img src="https://img.shields.io/badge/KDD%202026-Conference-2563eb?style=flat-square" /> [![](https://img.shields.io/github/stars/WillDreamer/FD-Bench?style=social&label=Code+Stars)](https://github.com/WillDreamer/FD-Bench)

- [**Omni-Mol: Multitask Molecular Model for Any-to-any Modalities**](https://arxiv.org/abs/2502.01074). Chengxin Hu, Hao Li, Yihe Yuan, Zezheng Song, Chenyang Zhao, and **Haixin Wang<sup>†</sup>**. <img src="https://img.shields.io/badge/NeurIPS%202025-Conference-2563eb?style=flat-square" /> [![](https://img.shields.io/github/stars/ChengxinHU/Omni-Mol?style=social&label=Code+Stars)](https://github.com/ChengxinHU/Omni-Mol)

- [**Recent Advances on Machine Learning for Computational Fluid Dynamics: A Survey**](https://arxiv.org/abs/2408.12171). **Haixin Wang**, Yadi Cao, Zijie Huang, Yuxuan Liu, Peiyan Hu, Xiao Luo, Zezheng Song, Wanjia Zhao, Jilin Liu, Jinan Sun, Shikun Zhang, Long Wei, Yue Wang, Tailin Wu, Zhi-Ming Ma, and Yizhou Sun. <img src="https://img.shields.io/badge/arXiv%202024-Preprint-b31b1b?style=flat-square" /> [![](https://img.shields.io/github/stars/WillDreamer/Awesome-AI4CFD?style=social&label=Code+Stars)](https://github.com/WillDreamer/Awesome-AI4CFD)

- [**PastNet: Introducing Physical Inductive Biases for Spatio-temporal Video Prediction**](https://dl.acm.org/doi/abs/10.1145/3664647.3681489). Hao Wu, Fan Xu, Chong Chen, Xian-Sheng Hua, Xiao Luo, and **Haixin Wang<sup>†</sup>**. <img src="https://img.shields.io/badge/ACM%20MM%202024-Conference-b31b1b?style=flat-square" /> [![](https://img.shields.io/github/stars/easylearningscores/pastnet?style=social&label=Code+Stars)](https://github.com/easylearningscores/pastnet)

- [**BENO: Boundary-embedded Neural Operators for Elliptic PDEs**](https://openreview.net/forum?id=ZZTkLDRmkg&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICLR.cc%2F2024%2FConference%2FAuthors%23your-submissions)). **Haixin Wang\***, Jiaxin Li\*, Anubhav Dwivedi, Kentaro Hara, and Tailin Wu. <img src="https://img.shields.io/badge/ICLR%202024-Conference-2563eb?style=flat-square" /> [![](https://img.shields.io/github/stars/AI4Science-WestlakeU/beno?style=social&label=Code+Stars)](https://github.com/AI4Science-WestlakeU/beno)

- [**Parameter-efficient Tuning of Large-scale Multimodal Foundation Model**](https://arxiv.org/abs/2305.08381). **Haixin Wang\***, Xinlong Yang\*, Jianlong Chang, Dian Jin, Jinan Sun, Shikun Zhang, Xiao Luo, and Qi Tian. <img src="https://img.shields.io/badge/NeurIPS%202023-Conference-2563eb?style=flat-square" /> [![](https://img.shields.io/github/stars/WillDreamer/Aurora?style=social&label=Code+Stars)](https://github.com/WillDreamer/Aurora)

- [**Towards Effective Domain Adaptive Retrieval**](https://ieeexplore.ieee.org/document/10042247). **Haixin Wang**, Jinan Sun, Shikun Zhang, Wei Xiang, Chong Chen, Xiansheng Hua, and Xiao Luo. <img src="https://img.shields.io/badge/IEEE%20TIP%202023-Journal-2563eb?style=flat-square" /> [![](https://img.shields.io/github/stars/WillDreamer/PEACE?style=social&label=Code+Stars)](https://github.com/WillDreamer/PEACE)

- [**Stacking Networks Dynamically for Image Restoration Based on the Plug-and-Play Framework**](https://link.springer.com/chapter/10.1007/978-3-030-58601-0_27). **Haixin Wang**, Tianhao Zhang, Muzhi Yu, Jinan Sun, Wei Ye, Chen Wang, and Shikun Zhang. <img src="https://img.shields.io/badge/ECCV%202020-Conference-b31b1b?style=flat-square" /> [![](https://img.shields.io/github/stars/WillDreamer/SND?style=social&label=Code+Stars)](https://github.com/WillDreamer/SND)



# 📄 Academic Services
- Reviewer for Conferences: KDD'23, ICCV'23, NeurIPS'23, AAAI'24, ICLR'24, SDM'24, CVPR'24, ECCV'24, ACM MM'24, ICLR'25, ICML'25, KDD'25, ACM MM'25, NeurIPS'25, AAAI'26, ICLR'26, KDD'26, CVPR'26.
- Reviewer for Journals: IEEE TIFS, Physics of fluids, IEEE TIP, IEEE TPAMI.




