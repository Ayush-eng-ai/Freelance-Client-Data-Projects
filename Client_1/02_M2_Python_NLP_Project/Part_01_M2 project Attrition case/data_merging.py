import pandas as pd

print("Loading data files...")
general_df = pd.read_csv('general_data.csv')
emp_survey_df = pd.read_csv('employee_survey_data.csv')
mgr_survey_df = pd.read_csv('manager_survey_data.csv')

print("Merging files...")
# EmployeeID ke basis par teeno files ko jod rahe hain
merged_df = pd.merge(general_df, emp_survey_df, on='EmployeeID', how='inner')
final_merged_df = pd.merge(merged_df, mgr_survey_df, on='EmployeeID', how='inner')

# Final file save kar rahe hain
final_merged_df.to_csv('Master_Merged_Data.csv', index=False)
print("Data merged successfully! Saved as 'Master_Merged_Data.csv'")