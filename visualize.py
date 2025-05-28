import matplotlib.pyplot as plt
import os
import uuid

def create_skill_plot(df):
    avg_scores = df[['math score', 'reading score', 'writing score']].mean()
    
    # Create plot
    plt.figure(figsize=(6, 4))
    avg_scores.plot(kind='bar', color='#5e63b6')
    plt.title('Average Scores by Subject')
    plt.ylabel('Score')
    plt.ylim(0, 100)
    
    # Save with unique filename
    filename = f'plots/skill_chart_{uuid.uuid4().hex}.png'
    full_path = os.path.join('static', filename)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    plt.savefig(full_path, bbox_inches='tight')
    plt.close()

    return filename
