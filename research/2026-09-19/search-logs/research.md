# Search branch: research accountability

Checked 2026-09-19. Starting point: arXiv 2605.21413v2 and its references.

Queries included: `"2605.21413" QuestBench writing evaluation`; `"DeepResearch Bench" report quality citation evaluation RACE FACT`; `"ResearchArena" evaluating deep research agents benchmark`; `2026 writing editing benchmark coherence factual preservation author voice`. Broad multi-query results were noisy. Followed primary-paper references and official repositories for inclusion.

Retained QuestBench as the anchor and DeepResearch Bench I/II for long-form report assessment. Read selected methods, evaluation and limitations sections; did not reproduce experiments.

Screened out generic browsing leaderboards, vendor/model launch pages and unrelated search results: they add little to writing instruction design. ResearchArena (Kang/Xiong, literature collection) was not included because source collection is already covered and the corpus prioritizes writing/editorial decisions. Do not confuse it with the 2026 auto-research project using the same name.

Checked the current data/license files for DeepResearch Bench II; per-task terms differ from the paper’s older blanket description. Raw GitHub URLs failed in web retrieval; canonical GitHub file pages were accessible. QuestBench’s HF viewer shows a schema error and missing card metadata; dependency license strings were not interpreted as a dataset license.

Arithmetic audit of QuestBench Table2: (57.58+52.94+31.82+35.14+32.43+32.26+30.95+22.73+25.26+16.67+15.23+12.50+7.81)/13 = 28.716923... . This checks a simple unweighted mean, not the authors’ unavailable raw aggregation. No corrected headline score is asserted.
