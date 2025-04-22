import pandas as pd

df = pd.read_csv("data/skill_builder.csv", usecols=['user_id'])
unique_users = df['user_id'].dropna().unique()

print("🔎 Sample User IDs:")
print(unique_users[:10])  # print the first 10 unique user IDs
