# visualize.py

import matplotlib.pyplot as plt
import pandas as pd
import os
import uuid

def create_skill_plot(df):
    # compute averages
    subjects = ['math score', 'reading score', 'writing score']
    averages = df[subjects].mean()

    # draw bar chart
    plt.figure(figsize=(8, 5))
    bars = plt.bar(subjects, averages, edgecolor='black')
    plt.title('Average Performance by Subject')
    plt.ylabel('Score (out of 100)')
    plt.ylim(0, 100)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval:.1f}', ha='center')

    # ensure the output directory exists
    out_dir = os.path.join('static', 'plots')
    os.makedirs(out_dir, exist_ok=True)

    # build filename and save
    filename = f"plot_{uuid.uuid4().hex[:8]}.png"
    filepath = os.path.join(out_dir, filename)
    plt.savefig(filepath, bbox_inches='tight')
    plt.close()

    # return the path *relative* to static/
    return f"plots/{filename}"
