import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/skill_builder.csv")

# Pick a user_id (you can also take input)
user_id = 61394

# Compute skill-wise accuracy
user_df = df[df['user_id'] == user_id]
skill_perf = user_df.groupby('skill')['correct'].mean().reset_index()
skill_perf.columns = ['skill', 'accuracy']
skill_perf = skill_perf.sort_values('accuracy')

# Plotting
plt.figure(figsize=(10, 8))
plt.barh(skill_perf['skill'], skill_perf['accuracy'], color='skyblue')
plt.xlabel("Accuracy")
plt.title(f"Skill Performance for User {user_id}")
plt.tight_layout()
plt.show()
