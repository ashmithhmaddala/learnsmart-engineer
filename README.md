# 📚 LearnSmart – AI-Powered Personalized Learning Recommender

**LearnSmart** is an AI-powered web app that analyzes student learning patterns and recommends personalized skill improvements based on past performance.

### 🔍 Features
- ✅ Upload and analyze real-world student data (SkillBuilder dataset)
- 📊 Visual charts for performance by skill
- 🤖 AI-based collaborative filtering to recommend new skills
- 🧠 Insights on weak concepts
- 🌐 Web interface built with Flask + HTML/CSS
- 📝 Logs every recommendation session for analysis

### 🚀 How it Works
1. Enter a user ID (or choose from sample ones)
2. View their skill-wise accuracy and progress
3. Get recommended next topics using AI
4. View performance trends on bar charts

### 🧰 Tech Stack
- **Backend**: Python, Flask
- **ML**: Collaborative Filtering, Pandas, Matplotlib
- **Frontend**: HTML, CSS (Vanilla)
- **Hosting Ready**: Can be deployed on Render / PythonAnywhere
- **Domain**: `learnsmart.engineer` 🌍

### 🧪 Sample User IDs
Try: `61394`, `78401`, `80439` or any real `user_id` in the dataset.

---

### 📂 Project Structure

```
recommendation-system/
├── app.py                # Flask app
├── model.py              # Skill performance analysis
├── recommend_ai.py       # Collaborative filtering engine
├── templates/index.html  # Main UI
├── static/chart.png      # Skill graph output
├── utils.py              # Misc helpers
├── logs/recommendation_log.csv  # Recommendation history
└── requirements.txt      # Dependencies
```

---

### ⚡ Getting Started

```bash
git clone https://github.com/ashmithhmaddala/learnsmart-engineer.git
cd recommendation-system
pip install -r requirements.txt
python app.py
```

> Open `http://127.0.0.1:5000` in your browser.

---

### 🧠 Future Ideas
- Add login system for teachers/students
- Track progress over time
- Recommend learning resources (videos/articles)
- Export charts as PDF

---

### 💡 Made with ❤️ by Ashmith Maddala
