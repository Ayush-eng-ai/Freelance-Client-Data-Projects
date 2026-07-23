import pandas as pd

print("Loading in_time and out_time files (isme 10-15 seconds lag sakte hain)...")
in_time = pd.read_csv('in_time.csv')
out_time = pd.read_csv('out_time.csv')

print("Calculating working hours...")
# First column ko 'EmployeeID' set kar rahe hain
in_time.rename(columns={in_time.columns[0]: 'EmployeeID'}, inplace=True)
out_time.rename(columns={out_time.columns[0]: 'EmployeeID'}, inplace=True)

in_time.set_index('EmployeeID', inplace=True)
out_time.set_index('EmployeeID', inplace=True)

# Time calculate karne ke liye Data format sahi kar rahe hain
in_time = in_time.apply(pd.to_datetime, errors='coerce')
out_time = out_time.apply(pd.to_datetime, errors='coerce')

# Out Time me se In Time minus karke Ghante (Hours) nikal rahe hain
hours = (out_time - in_time) / pd.Timedelta(hours=1)

# Har employee ka Average Working Hours nikal rahe hain
avg_hours = hours.mean(axis=1).reset_index()
avg_hours.rename(columns={0: 'Average_Working_Hours'}, inplace=True)

print("Merging with Master Data...")
master_df = pd.read_csv('Master_Merged_Data.csv')
final_df = pd.merge(master_df, avg_hours, on='EmployeeID', how='left')

# Final Data Save karna
final_df.to_csv('Final_M2_Dataset.csv', index=False)
print("Success! 'Final_M2_Dataset.csv' is ready with all data and working hours.")