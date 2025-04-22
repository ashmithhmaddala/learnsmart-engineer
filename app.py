from flask import Flask, jsonify
import pandas as pd
from model import get_user_performance, get_weak_skills
from flask import render_template, request
import matplotlib.pyplot as plt
from recommend_ai import recommend_skills
import csv
from datetime import datetime

app = Flask(__name__)

# Load once at startup
df = pd.read_csv("data/skill_builder.csv")

from model import get_user_performance, get_weak_skills, get_sample_user_ids

@app.route('/')
def home():
    sample_ids = get_sample_user_ids(df)
    return render_template("index.html", skills=None, ai_recs=[], sample_ids=sample_ids)

@app.route('/recommend/<int:user_id>', methods=['GET'])
def recommend(user_id):
    try:
        recs = get_user_performance(df, user_id)
        return jsonify({
            "user_id": user_id,
            "recommended_skills": recs
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/performance/<int:user_id>', methods=['GET'])
def performance(user_id):
    try:
        perf_df = get_user_performance(df, user_id)
        data = perf_df.to_dict(orient='records')
        return jsonify({
            "user_id": user_id,
            "performance": data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/show', methods=['POST'])
def show():
    user_id = int(request.form['user_id'])
    recs = get_weak_skills(df, user_id)
    ai_recs = recommend_skills(user_id, top_n=5) or []  # Ensure ai_recs is not None

    perf_df = get_user_performance(df, user_id)
    plt.figure(figsize=(10, 8))
    plt.barh(perf_df['skill'], perf_df['accuracy'], color='skyblue')
    plt.xlabel("Accuracy")
    plt.title(f"Skill Performance for User {user_id}")
    plt.tight_layout()
    plt.savefig('static/chart.png')  # Save the plot to the static folder
    plt.close()

    with open('logs/recommendation_log.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            user_id,
            '; '.join(recs),
            '; '.join(ai_recs),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])

    return render_template("index.html", skills=recs, ai_recs=ai_recs)

@app.route('/ai-recommend/<int:user_id>', methods=['GET'])
def ai_recommend(user_id):
    try:
        ai_recs = recommend_skills(user_id, top_n=5)
        return jsonify({
            "user_id": user_id,
            "ai_recommended_skills": ai_recs
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
