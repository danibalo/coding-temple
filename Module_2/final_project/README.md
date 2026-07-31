# Module 2 Project: Data Processing Pipeline
## TO DO
- There is a given messy employee survey dataset (messy_employee_survey.csv). I am going to implement DataPipeline class in pipeline.py so that running main.py produces a clean dataset, summary, and visualizations.

## Files
| File | Task |
|:------|:-----|
|pipeline.py | implements all methods in DataPipeline |
|main.py | summary printout |
| output| pipeline will save charts and cleaned CSV here

## Excepted Output
When complete, the pipeline should produce:
  - console output with a cleaning summary and analysis results
  - output/charts.png -- at least 2 visualizations
  - output / clean_employees.csv -- the cleaned dataset
## Data issues handled 
| Column | Issues|
|:----------|:--------|
|employee_id | Some duplicate IDs |
|name | Inconsistent casing, extra whitespace |
|department| Variants: "Eng", "ENGINEERING", "Engineering"|
|office_location| Variants: "NYC","New York", "new york" |
|salary | Stored as " $75, 000.00" strings, some negative, some missing"|
|years_experience | Some missing, one value > 50 (outlier)|
|satisfaction_score| should be 1 -10; some outside range, some missing |
|survey_date| Three differentt date formats mixed together|


