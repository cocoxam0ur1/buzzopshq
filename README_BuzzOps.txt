# BuzzOps HQ

BuzzOps HQ is a lightweight, Facebook-focused social media scheduler and analytics dashboard built for small businesses like Chalk Talk with Angela.

## 💡 Features
- Schedule Facebook posts via calendar input
- Archive and view post history
- Log engagement metrics (likes, comments, shares)
- View engagement history and analytics charts
- Offline use with built-in SQLite database

## 🛠 Requirements
- Python 3.9+
- pip packages:
  - matplotlib

Install dependencies:
```
pip install matplotlib
```

## 🚀 How to Run
1. Launch the application:
```
python main.py
```

2. Use login credentials:
- **Username:** test
- **Password:** test

3. Schedule posts, log engagement, and explore analytics.

## 📦 Creating an Executable
Use PyInstaller to bundle BuzzOps HQ:
```
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

Copy `buzzops.db` to the same directory as the executable.

## 🗃 Database
- **Posts:** id, caption, post_date
- **Engagement:** id, post_id, likes, comments, shares

## 📈 Analytics
Visualizes likes, comments, and shares for up to 5 recent posts using a stacked bar chart.

## 📞 Contact
Built by Team BuzzOps (Coco Sidock, Timothy Smith, Tuyet Nguyen)

Sponsor: Angela Sidock — Chalk Talk with Angela