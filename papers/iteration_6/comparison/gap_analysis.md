# Iteration 6 Gap Analysis

## Paper: Keratoconus Risk Factors Case-Control Study (All of Us Database)

---

## Gap 1: Missing Translational Relevance / Clinical Impact Statement
**Severity**: Medium
**Dimension affected**: Completeness, Clinical Relevance

**Description**: The original paper includes a "Translational Relevance" section in the abstract, which is a TVST journal-specific requirement. More broadly, the original concludes with a direct clinical message: "providers should be aware of all disease risk factors to aid in early diagnosis and intervention." The draft's Conclusions are more academic and less clinically actionable.

**Proposed Rule**:
> **[Iter6]** When the extracted data bundle indicates the study aims to identify risk factors for a condition, the Conclusions section should include an explicit clinical action statement (e.g., "Clinicians managing patients with [condition X] should be aware of [risk factor Y] to facilitate earlier screening and diagnosis"). Avoid purely academic conclusions that only call for "further investigation" without a concrete clinical takeaway.

---

## Gap 2: Verbosity in Discussion -- Speculative Mechanistic Content
**Severity**: Medium
**Dimension affected**: Readability

**Description**: The draft Discussion is approximately 50-60% longer than the original. Much of this excess comes from speculative mechanistic explanations drawn from general knowledge (e.g., detailed paragraphs on AGEs, leptin, floppy eyelid syndrome) that go beyond what the study data can support. The original is more tightly written, focusing on mechanisms directly referenced in its cited literature.

**Proposed Rule**:
> **[Iter6]** Limit speculative mechanistic discussion to 2-3 sentences per topic. When introducing pathophysiological hypotheses from general knowledge, use one sentence to state the mechanism and one to note its limitations. Avoid multi-sentence elaborations on mechanisms that the study did not directly test. If the extracted data bundle does not provide cited evidence for a mechanism, keep it brief with a [REF] placeholder.

---

## Gap 3: Missing Specific Detail on Most Common Medications Within Categories
**Severity**: Low-Medium
**Dimension affected**: Completeness, Clinical Relevance

**Description**: The original specifies that "The most common estrogen-containing medication reported in our cohorts was oral contraceptive pills." This clinical detail helps readers understand the real-world exposure and is missing from the draft. Similarly, for tetracyclines, the original provides specific indications (ocular rosacea, sterile corneal ulcerations).

**Proposed Rule**:
> **[Iter6]** When the extracted data bundle provides details about the most common specific agent or indication within a grouped medication variable (e.g., "most common estrogen-containing medication was oral contraceptive pills"), include this detail in either the Results or Discussion. Such specifics enhance clinical interpretability and should not be omitted as minor detail.

---

## Gap 4: Missing Appendix/Supplementary Analysis References
**Severity**: Low-Medium
**Dimension affected**: Completeness

**Description**: The original references appendix tables (Table A1, Table B1, Table B2) containing univariable results and ungrouped analyses. The draft mentions in the Limitations that univariable ORs were "not available for inclusion" but does not reference the appendix tables where they were presented. This omission makes it unclear to the reader that additional analyses were performed.

**Proposed Rule**:
> **[Iter6]** When the extracted data bundle mentions that supplementary or appendix tables contain additional analyses (e.g., univariable results, ungrouped sensitivity analyses), reference these in the Results section using the format "Additional results are presented in Appendix Table X" even if the appendix data itself was not extractable. This signals to the reader that additional analyses were conducted, consistent with the existing [Iter5] rule on supplementary material references.

---

## Gap 5: Disease Stage / Severity Considerations in Limitations
**Severity**: Medium
**Dimension affected**: Clinical Relevance

**Description**: The original explicitly notes that "the average age of participants in the KC cohort was 58.7 years. Because onset of the disease typically occurs in the second or third decade of life, it is likely that these patients have established, non-progressive KC." This has important clinical implications: risk factors identified may be less relevant for disease progression if the population has already-static disease. The draft's Limitations section does not address this.

**Proposed Rule**:
> **[Iter6]** When the study population's average age or disease duration suggests that participants are well past the typical onset/progression window for the condition under study, include this as a specific limitation. Note the implications for interpreting risk factor associations (e.g., factors may be correlates of established disease rather than drivers of onset/progression). This is clinically important for conditions with age-dependent natural history like keratoconus, myopia, or glaucoma.

---

## Gap 6: Coding System Specificity (SNOMED-CT)
**Severity**: Low
**Dimension affected**: Completeness

**Description**: The original specifies that KC cases were identified using "Systemized Nomenclature of Medicine, Clinical Terms (SNOMED-CT)" in addition to ICD codes. The draft mentions only "standardized medical terminology and International Classification of Diseases (ICD) codes." While acceptable, specifying the exact coding system is important for reproducibility.

**Proposed Rule**:
> **[Iter6]** When the extracted data bundle specifies the clinical terminology or classification system used for case identification (e.g., SNOMED-CT, ICD-10-CM, Read codes), name the system explicitly in the Methods. Do not generalize to "standardized medical terminology" if a specific system is named.

---

## Gap 7: Discussion Order -- Novel vs. Known Findings
**Severity**: Low-Medium
**Dimension affected**: Logical Flow, Clinical Relevance

**Description**: The original Discussion strategically leads with novel findings (estrogen, tetracycline) before covering known risk factors (OSD, obesity). The draft Discussion leads with OSD (strongest association statistically) and covers novel findings in the middle. The original's approach is arguably better for a paper whose primary contribution is identifying NEW associations, as the title suggests ("Exploring New Links"). Leading with the strongest statistical finding (OSD) is defensible but de-emphasizes the paper's novel contribution.

**Proposed Rule**:
> **[Iter6]** When the extracted data bundle indicates that the study's primary contribution is identifying novel associations (as suggested by study aims or framing), consider leading the Discussion with novel findings rather than strongest-association findings. If the study's stated purpose is to explore "new links" or "novel risk factors," the Discussion should foreground these. Known confirmatory findings can be discussed subsequently as validation of the study methodology.

---

## Summary of Proposed Rules

| # | Tag | Rule Summary | Severity | Dimension |
|---|-----|-------------|----------|-----------|
| 1 | [Iter6] | Include explicit clinical action statement in Conclusions | Medium | Clinical Relevance |
| 2 | [Iter6] | Limit speculative mechanistic discussion to 2-3 sentences per topic | Medium | Readability |
| 3 | [Iter6] | Include specific medication/agent details when available in bundle | Low-Medium | Completeness |
| 4 | [Iter6] | Reference appendix/supplementary tables for additional analyses | Low-Medium | Completeness |
| 5 | [Iter6] | Address disease stage/severity implications of population age | Medium | Clinical Relevance |
| 6 | [Iter6] | Name specific clinical coding systems (SNOMED-CT, ICD-10-CM) | Low | Completeness |
| 7 | [Iter6] | Lead Discussion with novel findings when that is the study's contribution | Low-Medium | Logical Flow |

**Total new rules proposed: 7**
