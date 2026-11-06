# Research papers and technical reports

Use this reference with SKILL.md. The report should be understandable and evaluable on its own. Supporting code establishes reproducibility; it should not be required to decode the prose.

## Focus on the final argument

- Use the known assignment rubric, publication requirements, audience, pronouns and length limit. Allocate space to methodological justification, evaluation and findings; do not spend the budget on an exhaustive experiment diary.
- Introduce the problem and questions, describe relevant data/preparation, explain methods/evaluation, present results and interpret limitations/conclusions. Fit the structure to the work instead of mechanically adding every possible section.
- Omit irrelevant failed attempts and corrected implementation mishaps unless they materially affect the interpretation of the final evidence. If a comparison is omitted, omit its counts/scores too; do not reuse them as though they evaluated the retained method.
- Keep the implemented process and the reported process aligned. If simplifying a historical procedure requires new research, explain that separately; prose alone cannot turn an adaptive process into a preplanned one.
- Motivate important choices using observed data or a stated practical rationale. A chosen duration, seed count or regularisation value need not be proved globally optimal. Do not invent such proof. Avoid using a method's sophistication as its justification.
- A concise account can omit a secondary selection exercise and report an actual fixed comparison, provided the reported features, scores and scope remain correct. Never rename a differently reduced model, hide a change in its inputs, or call its score independent when it was selected on those same data.

## Explain the actual method before its settings

- Begin with what a method does and why it is useful; then give settings needed to understand or reproduce it. An equation needs definitions for its symbols, inputs, units and applicable dates. Include a representative worked example where abstraction would otherwise obscure an important feature.
- Explain unfamiliar terms once. For example: an encoder learns a mapping from categories to numerical columns; a penalty discourages large coefficients; random seeds determine random training choices. “Average predictions across runs” is accurate; “average seeds” is not.
- Do not replace exact methods with an easier but incorrect label. A spline transformation creates smoothly connected polynomial pieces; it is not just a cubic power. A weak or zero importance score alone does not establish that a feature is a mistake.
- Explain before/after treatment for core fields and representative important engineered features. Simple categorical normalisation and retention of a raw measurement should not be oversold as sophisticated transformations.
- Acknowledge material source-availability exceptions plainly. “We use supplied economic observations from the prediction period” is clearer than an unexplained “known-covariate setting.” A one-month lag relative to a predicted month does not necessarily make that value available at a much earlier forecast date.

## Make evaluation understandable

- State full date ranges, including start and end months. “Through December” is insufficient if the reader may confuse a full-history fit with a short recent window. Describe material exceptions where relevant, without repeatedly interrupting every result with them.
- Distinguish calendar-month counts, elapsed duration and forecast horizon. If train/test dates overlap, do not call the entire test period strictly later. Use measured counts to explain a partial overlap when it matters; do not infer exact days from month-only records.
- For each period, state its role using concrete verbs: fit preprocessing/base models; generate predictions; fit combination weights; choose features/removals/settings; evaluate the chosen method; refit using all available labels. The word “validation” alone cannot communicate these different roles.
- If there are two holdout periods, explain which fitted object uses which answers and why the periods are separate. Base-model fitting and combination-weight fitting are different operations. Do not describe three months of model predictions as three months of total base-model training.
- The selection period chooses the variant; a later assessment checks the chosen variant. State the actual consequence of that assessment. Do not suggest a second selection took place if it did not, or create unnecessary extra evaluation stages in a writing task.
- After final refitting, earlier holdout answers may become fitting data; the prior score does not evaluate the refitted model on unseen answers. A different fitted subset or procedure cannot inherit another model's score.
- Explain adaptive reuse plainly: “We repeatedly checked the same validation results to decide what to try next.” No direct use of its labels in a single fit does not make that period untouched after repeated model selection. Public leaderboard feedback can also guide selection.
- Describe the direction and scale of the metric. Separate signed mean error, absolute error and RMSE. Low group-average error can hide large individual mistakes. Report consistent comparable scores, without universal optimality or unsupported significance claims.

## Make results tables explicit

- Identify the exact models/features and evaluation period. “Selected reduced set” and “earlier diagnostic” need concrete descriptions; use the actual change, such as “without economic indicators.” Baselines with fewer inputs should be labelled as such.
- For add/remove ablations, explain: additions start from a stated basic set; removals start from a stated full set; each changed model is retrained; comparisons use its relevant control. Use grouped table headers if this makes the two experiments immediately apparent. A negative RMSE change means improvement in either column.
- Give relevant findings next to labelled tables/figures and reference the actual object supporting the claim. A coefficient chart is not a chart of forecasts. Do not scatter unlabelled score statements through prose or repeat the table's full contents.
- Respect existing orientation and the user's requested edit. In LaTeX, `table*` spans two columns but a natural-width `tabular` can remain narrow; `tabular*` with `\textwidth` and stretchable spacing can fill the width without scaling the font. Do not widen every table by default.
- Keep controls, variants and scores aligned if shortening a table. An entry marked “not assessed” is a missing evaluation, not a poor result. Avoid inserting unnecessary stages merely to make row counts symmetric.

## Interpret errors and model explanations carefully

- Built-in tree importance measures the fitted model's prediction behaviour; its percentages are not automatically performance gains or explained variance. Name the actual measure or describe it accurately.
- Group permutation rearranges that group's columns between records using the same row permutation for those columns, leaves outcomes/other inputs fixed, and evaluates the existing model without retraining. A refitted removal ablation instead measures what happens after learning without the inputs. If the implementation differs, describe the implementation rather than this example.
- Verify which feature/group ranks highest for each measure. An individual calendar variable may rank first internally while a property group causes the largest permutation error. These do not justify claiming both charts identify the same single winner.
- A category containing many rare cases may still contain very few rare cases as a fraction of its own records. State both denominators where necessary. Low prevalence does not prove classification is impossible, and unknown test targets do not prevent learning a classifier from training labels.
- Identical recorded predictors with differing outcomes suggest unrecorded explanatory factors. They do not establish a particular cause, prove all matching records are duplicate errors, or quantify an attainable error floor. Avoid claiming that missing information or an observed slice necessarily explains all remaining error.

## Keep the final document concise and coherent

- Describe fitting and selection in Methods, compare outcomes in Results, and explain remaining limitations in Discussion. Do not repeat a removal path, date schedule or caveat in every section. Put importance/permutation alongside feature-contribution analysis when that gives a clearer flow; section names should reflect their actual contents.
- Mention only the analysed period in an error table's introduction if the fitting schedule is already clear. Distinguish selection-period error analysis from an independent evaluation once, in a sentence that directly affects interpretation.
- Conclusions answer the stated questions, summarise the final fitting procedure and result, and explain the main learning and material limitations. Do not reintroduce discarded variants or implementation trivia.
- Use related work to support concrete methodological choices; verify citations rather than fabricate them. A report should not tell readers to inspect a notebook to understand an essential method or conclusion. Reproducibility references can be brief and separate from the argument.
- Use appendices for useful supporting detail, not repeated main text. Give them clear lettered headings, unique labels and valid references. Check that a shortened main section still refers to the correct surviving table/figure. Keep mathematical syntax compatible with the intended renderer.
- For critical-error reviews, prioritise wrong numbers, unsupported conclusions, mismatched model/score attribution, missing availability assumptions and misleading evaluation claims. Do not burden the user with optional stylistic changes or requests to restore every omitted experiment.
