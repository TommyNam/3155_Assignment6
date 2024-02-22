from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

def days_until_halloween():
    today = datetime.today()
    halloween = datetime(today.year, 10, 31)
    if today > halloween:
        halloween = datetime(today.year + 1, 10, 31)
    days_left = (halloween - today).days
    return days_left

@app.route('/')
def countdown():
    days_left = days_until_halloween()
    return render_template('index.html', days_left=days_left)

if __name__ == '__main__':
    app.run(debug=True)
