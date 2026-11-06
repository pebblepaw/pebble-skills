---
name: clear-analytics-writing
description: Write, explain, or revise analytical prose in reports, research papers, notebooks, READMEs, presentations and chat. Use for plain-English methods, meaningful charts and tables, evidence-backed conclusions and focused reviews. Preserve technical accuracy, the reader's context and the user's requested editing scope.
---

# Clear analytics writing

Write so a reader seeing the work for the first time can understand **what we did, why, what the evidence shows and what follows from it**. The goal is an understandable argument, not an inventory of everything performed. Use these principles across formats; load only the format-specific guidance needed below.

## Establish the scope before writing

- Follow the current request: explanation, targeted fixes, replacement prose, or file edits. A request for chat wording does not authorize editing an artifact. A writing task does not authorize new experiments or changes to the methodology.
- Read the latest passage and relevant context when the user says they edited it. Preserve their local edits, chosen terminology, acceptable structure and table orientation. Adding a column should not become a table redesign.
- Reuse known audience, pronouns, page limit and constraints. Ask only for missing information that affects the work. Do not repeatedly ask preferences already established in the conversation.
- Match the requested response size. For a yes/no check, answer directly and give only necessary corrections. For a critical-errors-only review, report only material errors. Do not turn it into a comprehensive rewrite or style critique.
- Verify technical claims against the actual calculations, outputs or implementation. If facts are unclear, say what is unverified; do not invent a convenient explanation for a decision or agree with an incorrect recollection.

## Make the meaning immediate

- Use concrete subjects, familiar verbs and complete sentences. Say who or what was measured and what operation was performed. Write “we predict each record's price,” not “each prediction concerns an observation.”
- Keep established project and source names. If supplied files are called auxiliary datasets, keep that name. Do not silently rename them reference tables. Distinguish a dataset's source from a feature group's purpose.
- Avoid mannered prose and compressed labels such as “transition identifier,” “later block,” “fixed recipe,” “local evidence” or “post-origin covariates” when the reader has not been told what they mean. Prefer “record ID,” “later holdout period,” “the model settings,” “earlier records for the same address,” or an explicit explanation of the information available at prediction time.
- Retain necessary scientific terms and define them at first use. Plain English must not change the method: a spline is not simply a cubed variable; regularisation strength is not an intercept. Use the shortest accurate description, with the exact library/function when useful.
- Be literal about fields and actions. A date records when something happened; it does not “place a record.” Software may learn parameters, but a field does not choose or decide. Replace decorative descriptions with the actual measured quantity.
- Use direct headings such as “Price distribution,” “Median price by location,” “Missing-value treatment” and “Model comparison.” Avoid theatrical headings, unexplained abbreviations, and titles framed around unnecessary negations.
- Prefer positive explanations. Use a contrast only to resolve a real misunderstanding or define an important boundary, rather than repeatedly stating what the work is not.
- Write coherent paragraphs. Use bullets for parallel items, especially **Field or feature name: explanation**. Avoid both dense chains of unrelated short sentences and long paragraphs that should be a list.
- Bold key phrases, results and decisions sparingly. Bolding an entire finding removes the visual hierarchy. Do not attach bolding to every sentence in ordinary prose.

## Build a clear argument, not a diary

- Explain a choice through its purpose, operation, evidence and consequence. A cleaning decision, transformation or result should not appear as an isolated slogan.
- Connect findings to their actual implications: retain an input, reject the tested variant, examine a possible issue, or conclude that evidence is insufficient to justify a change. “No change is justified” is a valid outcome. Do not invent an action, an experiment or an improvement to make a paragraph feel complete.
- State a research question's answer directly where questions are used. Do not impose a question-and-answer format on every notebook, report or explanation.
- Give each section one job. Describe the method once, present its result where relevant, and discuss its meaning without repeating the procedure. An error-analysis table for one period usually needs that period named, not another full account of how earlier fitting data were used.
- A final account need not include every abandoned experiment, corrected implementation mistake, handoff or intermediate model. Omit immaterial history. Keep any detail whose omission would misrepresent the implemented method, selection process, evidence or result.
- Do not turn separate research comparisons into an invented sequential pipeline. A later explanatory ablation did not necessarily generate the earlier candidate models. If chronology matters, state it accurately; otherwise describe each comparison by its purpose.
- Keep infrastructure details out of the main analytical story unless needed by the audience: hashes, internal task codes, branches, ownership, promotion rules and local-cache status usually belong in reproducibility material or operational documentation.
- A candidate, a final model and a diagnostic comparison are different things. Name the one being discussed. “All features” means all features in a specified comparison, not every input ever explored.

## Make quantities and comparisons unambiguous

- Identify the object being counted: records, unique entities, repeated descriptions, columns, feature groups, model variants, or training runs. Do not switch between them without explaining the relationship. If that relationship adds no useful insight, omit the extra count rather than create another label.
- State a percentage's denominator. “Most rare cases occur in category A” does not mean “most category A records are rare.” Neither statement establishes how many predictions were correct.
- State the control, period, metric, units and direction for each important comparison. Explain what a positive or negative change means. A numerical difference is useful only when the compared quantities support that interpretation.
- Separate input information from observed outcomes; feature-source categories from semantic feature groups; individual records from aggregated summaries; numerical correlation from categorical associations.
- Compare methods on the same records and split when claiming an accuracy improvement. If inputs or fitting policies differ, make that visible. Do not subtract results from different periods or test populations and call the difference a model improvement.
- Tables should explain themselves: clear row names, informative column headings, units, and explicit missing entries such as “not assessed” where appropriate. Do not invent a score for an untested variant or use “diagnostic” as a substitute for naming what was tested.
- Preserve the requested layout. Grouped headers can distinguish “add to basic features” from “remove from full features.” Keep a baseline's restricted inputs visible even if its unchanged score is repeated across rows.
- Prefer one representative worked example to several unexplained methods. Show the actual input, calculation and output. Use a nonmissing example that demonstrates the operation; distinguish illustrative numbers from measured results.

## Preserve the limits of the evidence

- Say “improved in this comparison” rather than “proved useful” for a small, context-dependent score difference. Better scores on one period do not establish a universal optimum or statistical significance.
- Falling training and validation errors do not prove the absence of overfitting. Strong correlation does not establish causation or incremental predictive benefit. Weak correlation does not establish uselessness for a nonlinear model.
- Error metrics describe errors: squared error emphasises large absolute misses, not inherently low target values. Signed average errors can cancel; low average bias is compatible with large individual errors.
- Verify which importance measure was computed and what it measures. Built-in model importance, permutation importance and refitted removal tests answer different questions; agreement must be checked rather than asserted. An importance percentage is not automatically explained variance or an accuracy gain.
- Describe a limitation in proportion to its effect, once where it helps interpretation. Do not bury the result in repeated disclaimers or omit a limitation essential to understanding the score.
- Explain heuristics honestly: a practical window or fixed setting is not an empirically established optimum unless compared. A failed variant does not rule out its entire research direction.
- Omit abandoned details without concealing the adaptive use of evaluation data when it affects the reported conclusion. Do not relabel a selection score as independent performance or imply an omitted procedure never happened when the claim depends on it.

## Format-specific guidance

### Jupyter notebooks

Read [references/notebooks.md](references/notebooks.md) when writing or reviewing notebooks. It covers visible calculations, before-and-after examples, chart observations, source coverage and readable executed outputs.

### Research papers and technical reports

Read [references/research-reports.md](references/research-reports.md) when drafting or reviewing a paper or report. It covers self-contained methods, time windows, selection and fitting, concise evidence, tables and appendices. Apply the relevant parts to nonacademic technical reports too.

### Other writing and short explanations

Use the general principles without imposing a research-paper structure. Put the answer or recommendation first, explain only terms needed for it, and give one concrete example if the concept remains abstract. For a dashboard, slide, README or business note, identify the reader's decision and retain only evidence and operating detail needed for that decision. Never add a new file or change a source artifact merely because this skill was invoked.

## Final reader-first checklist

Before delivering, check the items relevant to the request:

- [ ] The latest source and the user's edits, requested format and response length are respected.
- [ ] A new reader can identify the subject, operation, comparison and takeaway without prior chat context.
- [ ] Source names and technical terms are consistent; necessary unfamiliar terms have a brief explanation.
- [ ] Dates, units, counts, denominators and positive/negative signs have explicit meanings.
- [ ] The claims agree with the code/calculations, displayed outputs and actual tested variant.
- [ ] Training, selection, evaluation and final fitting are distinguished wherever their roles affect a claim.
- [ ] A selected model's score has not been borrowed from another period, model or fitting procedure.
- [ ] Every included figure/table answers a question or supports a useful point, with a clear interpretation.
- [ ] The finding leads to a justified implication; there is no invented action, cause, proof or optimality claim.
- [ ] No redundant procedure, discarded history or operational detail distracts from the requested explanation.
- [ ] The wording describes what happened directly, without invented labels, unnecessary negations or dense lists disguised as prose.
- [ ] Tables retain the requested orientation; labels, legends, references and rendered text remain readable.

Ask: **What is this? What did we do? Compared with what? What did we learn? Why does it matter?** If the reader must reconstruct these answers, revise or remove the passage.
