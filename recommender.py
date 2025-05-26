def generate_recommendations(df):
    # Calculate average scores for each subject
    df['average'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

    # Identify weakest subject per student
    def find_weakest(row):
        scores = {
            'Math': row['math score'],
            'Reading': row['reading score'],
            'Writing': row['writing score']
        }
        weakest = min(scores, key=scores.get)
        return weakest

    df['weakest_subject'] = df.apply(find_weakest, axis=1)

    # Count how often each subject is the weakest (insight)
    recommendation_summary = df['weakest_subject'].value_counts().to_dict()

    # Return as a friendly list of recommendations
    recommendations = [
        f"Focus on improving {subject} — identified as the weakest in {count} students"
        for subject, count in recommendation_summary.items()
    ]

    return recommendations
