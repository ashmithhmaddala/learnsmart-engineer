from flask import Flask, request, render_template, url_for
import pandas as pd
from recommender import generate_recommendations
from visualize import create_skill_plot
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Recommendation route
@app.route('/recommend', methods=['POST'])
def recommend():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400

    df = pd.read_csv(file)

    # Generate recommendations and chart path
    recommendations = generate_recommendations(df)
    chart_path = create_skill_plot(df)  # This should return something like 'images/chart.png'

    return render_template(
        'results.html',
        recs=recommendations,
        chart=url_for('static', filename=chart_path)
    )

if __name__ == '__main__':
    app.run(debug=True)
