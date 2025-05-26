import matplotlib.pyplot as plt
import pandas as pd
import os
import uuid

def create_skill_plot(df):
    # Calculate average scores across all students
    subjects = ['math score', 'reading score', 'writing score']
    averages = df[subjects].mean()

    # Plot settings
    plt.figure(figsize=(8, 5))
    bars = plt.bar(subjects, averages, edgecolor='black')
    plt.title('Average Performance by Subject')
    plt.ylabel('Score (out of 100)')
    plt.ylim(0, 100)

    # Label bars with exact values
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 2, f'{yval:.1f}', ha='center')

    # Save to static folder
    plot_id = str(uuid.uuid4())[:8]
    plot_path = f'static/plot_{plot_id}.png'
    plt.savefig(plot_path, bbox_inches='tight')
    plt.close()

    return plot_path