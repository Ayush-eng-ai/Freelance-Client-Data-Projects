import pandas as pd

print("Loading E-commerce comments data...")
# Sahi file ka naam use kar rahe hain
try:
    df = pd.read_excel('ecom data reduced.xlsx')
except Exception as e:
    print(f"Error: {e}")
    exit()

print("Building AI Model to segregate comments...")
# Data mein label1 ka matlab Negative aur label2 ka matlab Positive hai
df['Sentiment_Category'] = df['Polarity'].map({'label1': 'Negative', 'label2': 'Positive'})

# Management ko Negative comments par focus karna hai, isliye hum unhe alag nikal rahe hain
negative_comments = df[df['Sentiment_Category'] == 'Negative']
positive_comments = df[df['Sentiment_Category'] == 'Positive']

print(f"Total Comments Processed: {len(df)}")
print(f"Positive Comments Found: {len(positive_comments)}")
print(f"Negative Comments Identified: {len(negative_comments)}  <-- (Action Required by Management)")

# Final segregated data ko save kar rahe hain
df.to_csv('Segregated_Comments.csv', index=False)
negative_comments.to_csv('Critical_Negative_Comments.csv', index=False)

print("\nModel successfully segregated comments!")
print("Saved 2 files: 'Segregated_Comments.csv' and 'Critical_Negative_Comments.csv'")