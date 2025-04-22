import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/skill_builder.csv")
df = df[['user_id', 'skill', 'correct']].dropna()

pivot_df = df.groupby(['user_id', 'skill'])['correct'].mean().reset_index()

user_enc = LabelEncoder()
skill_enc = LabelEncoder()

pivot_df['user_idx'] = user_enc.fit_transform(pivot_df['user_id'])
pivot_df['skill_idx'] = skill_enc.fit_transform(pivot_df['skill'])

num_users = pivot_df['user_idx'].nunique()
num_skills = pivot_df['skill_idx'].nunique()

ratings_matrix = pd.DataFrame(0.0, index=range(num_users), columns=range(num_skills), dtype=float)
for row in pivot_df.itertuples():
    ratings_matrix.at[row.user_idx, row.skill_idx] = row.correct

svd = TruncatedSVD(n_components=15, random_state=42)
predicted = svd.fit_transform(ratings_matrix)
pred_matrix = svd.inverse_transform(predicted)
pred_df = pd.DataFrame(pred_matrix, index=ratings_matrix.index, columns=ratings_matrix.columns)

def recommend_skills(user_id, top_n=5):
    try:
        uid = user_enc.transform([user_id])[0]
        user_scores = pred_df.loc[uid]
        seen_skills = pivot_df[pivot_df['user_idx'] == uid]['skill_idx'].tolist()
        user_scores[seen_skills] = -1
        top_indices = user_scores.sort_values(ascending=False).head(top_n).index
        skill_names = skill_enc.inverse_transform(top_indices)
        return skill_names.tolist()
    except Exception:
        return []

if __name__ == "__main__":
    sample_user_id = 61394
    recs = recommend_skills(sample_user_id, top_n=5)
    print(f"🔮 AI Recommendations for User {sample_user_id}:", recs)
