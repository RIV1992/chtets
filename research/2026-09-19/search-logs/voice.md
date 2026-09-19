# Voice, collaboration and multilingual register: search log

Checked 2026-09-19. This is a targeted, non-exhaustive review for candidate Chtets instructions, not an efficacy evaluation of Chtets. All annotations are original summaries. No corpus rows or paper text are redistributed.

## Search approach

Used web search to identify original papers, followed by publisher/ACL/arXiv full-text sections and author-maintained resource pages. Many search results were unrelated, and some returned domain-home URLs rather than article URLs. Those snippets were not treated as verification. Verified article identifiers were opened directly; where unavailable, the limitation is recorded per source.

Query families included:

- `CoAuthor dataset human AI collaborative writing 2022 paper`
- `XFORMAL benchmark multilingual formality style transfer French 2021 paper`
- `STYLL style transfer language models author imitation paper`
- `STYLL authorship style transfer Patel 2023`
- `LaMP When Large Language Models Meet Personalization`
- `Dear Sir or Madam, May I Introduce the GYAFC Dataset`
- `Generative AI enhances individual creativity but reduces the collective diversity of novel content`
- `Doshi Hauser generative creativity novel content 2024`
- `adn5290 Dryad`
- `XFORMAL github license`
- `CoAuthor github license Stanford`
- `Russian authorship style transfer personal writing voice benchmark Russian`

Follow-up section searches targeted human evaluation, meaning preservation, hallucination, ownership, limitations, dataset rights and licenses. Each source record identifies inspected sections, including preprint/final-version distinctions. Paper resource access was checked; benchmark contents were not comprehensively audited or used to train anything.

## Inclusion and prioritization

Six primary studies retained. Core: CoAuthor, XFORMAL, STYLL, Doshi–Hauser. Extended: GYAFC as an English evaluation foundation and LaMP as an adjacent retrieval/personalization benchmark. STYLL has a directly useful documented failure case, but its publication status is marked conservatively as an arXiv preprint because a peer-reviewed venue was not verified.

## Exclusions and deferred candidates

- General personalization perspective paper arXiv:2307.16376 is distinct from LaMP; excluded to avoid conflating a perspective article with the empirical benchmark.
- ResearchGate, press coverage, generated Hugging Face summaries and commercial product pages were discovery leads only, not evidential sources.
- A GYAFC supplementary PDF returned a confidential-review banner; it was not used. Public published paper and official resource page suffice.
- TinyStyler (EMNLP 2024, arXiv:2406.15586) is a useful later voice-transfer candidate. Deferred to keep this collection focused on transferable workflow and evaluation rather than adding another model architecture.
- HyperStyler (arXiv:2609.02772) and a 2025 persona-diversity preprint (arXiv:2504.13868) appeared during search but were not fully inspected. They are leads for a later update, not support for present rules.
- Speech anti-spoofing, text-to-image cultural benchmarks and authorship-attribution-only tools do not directly validate preserving a writer's meaning and voice; excluded.

## Gaps and boundaries

- French is directly covered by XFORMAL for sentence-level register. This does not establish preservation of one person's voice in French, or genre-appropriate business correspondence.
- No sufficiently direct Russian author-voice-preservation study was verified in this targeted search. This is a coverage gap, not a claim that no such research exists. Russian and French need original evaluation briefs and competent human reviewers.
- The studies predominantly concern older models, short text and specific domains. They cannot validate a modern portable prompt across all agents.
- Personalization scores, author-classifier confusion, requested formality, factual fidelity, perceived ownership and collective diversity are distinct targets. No single metric should stand in for all six.
- Style samples are not fact sources for new texts. Candidate rules explicitly mark the move from reported findings to practical skill design as inference.
- Corpus access and redistribution rights are distinct. XFORMAL is conditional on Yahoo access and academic permissions; GYAFC is author-mediated; LaMP code is noncommercial and constituent datasets differ. Link and summarize; do not copy these datasets into a permissively licensed skill repository.
- No mitigation of homogenization is claimed proven here. The candidate diversity workflow is a testable design proposal.
