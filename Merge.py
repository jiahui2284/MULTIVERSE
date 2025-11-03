import pandas as pd

# --- Load all uploaded CSV files ---
jobs_ffwd = pd.read_csv("Bjobs.csv")
jobs = pd.read_csv("Alltechjobs.csv")
jobs1 = pd.read_csv("Alltechjobs1.csv")
jobs2 = pd.read_csv("Alltechjobs2.csv")
jobs3 = pd.read_csv("Alltechjobs3.csv")
jobs4 = pd.read_csv("Alltechjobs4.csv")
jobs5 = pd.read_csv("Alltechjobs5.csv")
jobs6 = pd.read_csv("Alltechjobs6.csv")
jobs7 = pd.read_csv("Alltechjobs7.csv")
jobs8 = pd.read_csv("Alltechjobs8.csv")
jobs9 = pd.read_csv("Alltechjobs9.csv")
jobs10 = pd.read_csv("Alltechjobs10.csv")
jobs11 = pd.read_csv("Alltechjobs11.csv")
jobs12 = pd.read_csv("Alltechjobs12.csv")
jobs13 = pd.read_csv("Alltechjobs13.csv")
jobs14 = pd.read_csv("Alltechjobs14.csv")
jobs15 = pd.read_csv("Alltechjobs15.csv")
jobs16 = pd.read_csv("Alltechjobs16.csv")
jobs17 = pd.read_csv("Alltechjobs17.csv")
jobs18 = pd.read_csv("Alltechjobs18.csv")
jobs19 = pd.read_csv("Alltechjobs19.csv")
jobs20 = pd.read_csv("Alltechjobs20.csv")
jobs21 = pd.read_csv("Alltechjobs21.csv")
jobs22 = pd.read_csv("Alltechjobs22.csv")
jobs = pd.concat([
    jobs, jobs1, jobs2, jobs3, jobs4, jobs5, jobs6, jobs7, jobs8, jobs9,
    jobs10, jobs11, jobs12, jobs13, jobs14, jobs15, jobs16, jobs17,
    jobs18, jobs19, jobs20, jobs21, jobs22
], ignore_index=True)
jungle_job = pd.read_csv("jobs_jungle_all_pages.csv")
aijobs_ai = pd.read_csv("aijobs_ai_US.csv")
jobs_80000hours = pd.read_csv("jobs_80000hours.csv")
council_jobs = pd.read_csv("council_jobs.csv")

# --- Function to standardize column names and select relevant columns ---
def standardize_df(df, col_mapping):
    df = df.rename(columns=col_mapping)
    # Keep only the relevant columns
    selected_cols = [c for c in ['job_title', 'company', 'location', 'job_link'] if c in df.columns]
    return df[selected_cols]

# --- Standardize each dataset ---

council_jobs_std = standardize_df(council_jobs, {
    'Job Title': 'job_title',
    'Organization': 'company',
    'Location': 'location',
    'Job Link': 'job_link'
})

jobs_ffwd_std = standardize_df(jobs_ffwd, {
    'Job Title': 'job_title', 
    'Company': 'company', 
    'Location': 'location', 
    'Job link': 'job_link'
})

jobs_std = standardize_df(jobs, {
    'Job Title': 'job_title', 
    'Company/Organization': 'company', 
    'Location': 'location', 
    'Job Link': 'job_link'
})

jungle_job_std = standardize_df(jungle_job, {
    'Job Title': 'job_title', 
    'Company': 'company', 
    'Location': 'location', 
    'Job Link': 'job_link'
})

aijobs_ai_std = standardize_df(aijobs_ai, {
    'Job Title': 'job_title', 
    'Company': 'company', 
    'Location': 'location', 
    'Job link': 'job_link'
})

jobs_80000hours_std = standardize_df(jobs_80000hours, {
    'Job Title': 'job_title', 
    'Company': 'company', 
    'Location': 'location', 
    'Job link': 'job_link'
})

# --- Concatenate all datasets ---
merged_jobs = pd.concat([
    jobs_ffwd_std, 
    jobs_std, 
    jungle_job_std, 
    aijobs_ai_std, 
    jobs_80000hours_std,
    council_jobs_std
], ignore_index=True)

merged_jobs_unique = merged_jobs.drop_duplicates(
    subset=['job_title', 'company', 'location', 'job_link'], keep='first'
)

output_path = "merged.csv"
merged_jobs_unique.to_csv(output_path, index=False)

print(f"Merged dataset saved to: {output_path}")
