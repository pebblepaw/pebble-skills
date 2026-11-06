# Notebook explanations and presentation

Use this reference with the general principles in SKILL.md. A notebook should let the reader follow the analysis, inspect representative calculations and verify the findings without reconstructing hidden project history.

## Tell one sequential story

- Organise by analytical purpose: understand the data, explain its preparation, show the important transformations, compare methods, inspect errors and reach conclusions. Adapt this structure to the task; do not force every notebook into a pure EDA template.
- Keep related explanations, code and outputs together. Do not show a summary transformation table before the reader has seen the calculation unless the summary genuinely aids orientation. Avoid duplicated sections or charts with no additional purpose.
- Use native Markdown cells for explanations and observations. Do not print paragraphs from Python. Use normal paragraphs or bullets separated by blank lines so Jupyter renders the intended structure.
- Bold a few words or a decisive number in each chart's observation, rather than the entire observation. Place observations after their corresponding outputs, with one interpretation for each panel where necessary.
- Reusable implementation can live in modules. Keep short, explanatory transformations and representative arithmetic visible in notebook cells when doing so helps readers understand what changed. Do not silently reorganise the source layout as part of prose editing.

## Show the data and its treatment

- Explain what one row represents before counting records or analysing duplicates. Distinguish exact repeated rows, repeated entities and identical predictor values with different outcomes. Do not assume repeated rows are either errors or independent real events without evidence.
- Introduce each source with its actual name, purpose, measured size/date coverage and role: explored only, used in a standalone comparison, used by a candidate, or retained in the final method. Cover material external inputs as well as supplied auxiliary inputs. Avoid a long source tour that never connects to the analysis.
- Describe cleaning as **Field name: count, action and reason**. Be explicit about whether a record was dropped, a column excluded, a sentinel converted to a missing value, a value imputed, or missingness retained for a model that supports it.
- Never change “missing cells” into “dropped rows.” A missing postal field need not imply deleting its entity. Converting a sentinel to NaN is only one stage: explain what the downstream method does with that missing value.
- Quantify actual problems instead of listing hypothetical checks as findings. Give a genuine problematic row or count where helpful. If no invalid values were found, say so without suggesting a repair occurred.
- Show readable dataframe tables for source fields, structured configuration contents and examples. Avoid raw lists of keys, dictionaries, console dumps, or truncated description columns when the reader needs the contents. Expand a format abbreviation once if it matters.
- Link prose feature names to actual column names. Present important transformations as **Feature (`column_name`): formula and purpose**, with the original and engineered values side by side.
- If a field was retained unchanged, say so: “Already measured in square metres; no conversion.” Avoid describing unchanged raw values as mysterious feature engineering.
- Show complete, useful examples: matched coordinates when discussing geographic joins; actual contributing historical records when discussing smoothing; intermediate values and final output for lagged averages. An all-missing example cannot demonstrate how a nonmissing feature is calculated.

## Make numerical claims verifiable

- A reported count, correlation, mean, feature total or score needs a visible calculation and saved output, or a clearly identified source measurement. A number in Markdown alone is not evidence. Compute it rather than type it into a print statement as though it were calculated.
- Calculate report figures/tables from the submitted analysis. Where notebooks are the promised evidence, ensure the report's material claims and sources are substantiated there. Do not hide unexplained precomputed charts in an unsubmitted experiment folder.
- Keep model caches and provenance available where reproduction needs them, while keeping hashes, local paths and ownership out of the analytical narrative. Label cache reuse accurately; do not present loading saved results as fresh training.
- On a substantive executable revision, rerun affected cells top to bottom when authorised and feasible. Check that Markdown interpretations still agree with outputs. Do not claim execution if only prose or syntax was checked.

## Design purposeful charts and tables

- Give each visual one main comparison, a literal title, readable axes/units and an explicit takeaway. Sort categories where it clarifies the comparison. Include useful benchmarks, average lines, direct value labels or counts.
- Choose a representation for the analytical question: time series for change over time; sorted bars for categories; heatmaps for correlation, missingness or signed add/remove comparisons; maps for meaningful geographic patterns. These are options, not mandatory plot types.
- Avoid crowded multiseries charts: choose representative series, small multiples or a justified summary. Use a signed-error plot when two large, nearly overlapping mean lines hide the difference the reader needs to see.
- Use vibrant, distinct colours with consistent meanings. Use diverging colours for signed changes, and do not rely on colour alone. Ensure annotations, legends, category labels and bars do not overlap. Increase margins, spacing and figure size or split panels as needed.
- Render and inspect modified charts when plotting is in scope. Correct code does not guarantee readable figures. Do not launch expensive retraining to check a layout change if existing verified plotting inputs suffice.
- Make tables interpretable: mark which dataset/group/column a row names; show full important descriptions; state what an unassessed score means. If training curves are included, identify both training and validation series and label the iteration/tree counts; choose lines, bars or panels according to readability.

## Explain what the analysis changed

- Correlations describe relationships. Explain whether a suspected duplicate was confirmed, retained because it represents a different construct, or tested for removal. Do not impose an automatic correlation threshold or imply an unperformed deletion.
- Distinguish grouped feature ablation from individual feature testing, and both from removing an ensemble member. State the initial feature set, control and refitting operation. Independent add/remove tests are not a cumulative search.
- An importance score motivates investigation, not automatic pruning. Correlated features can substitute for each other; negative ensemble coefficients can correct shared errors. State which claim the actual refitted comparison supports.
- A result without a change can still be useful: it may rule out the tested change or show that the evidence is too weak. Say that explicitly rather than promising additional modelling merely to complete the narrative.
