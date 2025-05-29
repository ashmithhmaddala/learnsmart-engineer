from flask import Flask, request, render_template, url_for
import pandas as pd
from recommender import generate_recommendations
from visualize import create_skill_plot

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    file = request.files.get('file')
    if not file or file.filename == '':
        return "No file uploaded", 400

    df = pd.read_csv(file)
    recs = generate_recommendations(df)
    chart_filename = create_skill_plot(df)
    chart_url = url_for('static', filename=chart_filename)

    return render_template(
        'results.html',
        recs=recs,
        chart=chart_url
    )

if __name__ == '__main__':
    app.run(debug=True)
