import pandas as pd

def get_user_performance(df, user_id):
    user_df = df[df['user_id'] == user_id]
    skill_perf = user_df.groupby('skill')['correct'].mean().reset_index()
    skill_perf.columns = ['skill', 'accuracy']
    return skill_perf.sort_values('accuracy')

def get_weak_skills(df, user_id, threshold=0.7):
    perf = get_user_performance(df, user_id)
    weak = perf[perf['accuracy'] < threshold]
    return weak['skill'].tolist()

def get_sample_user_ids(df, limit=10):
    return df['user_id'].dropna().unique()[:limit].tolist()
