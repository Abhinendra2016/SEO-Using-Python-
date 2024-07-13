import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from flask import Flask, request, render_template, redirect, url_for, flash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your_secret_key')

# Your JSON  Key FILE goes here
SERVICE_ACCOUNT_FILE = 'smooth-pen.json'

# Indexing API
SCOPES = ["https://www.googleapis.com/auth/indexing"]

# Credentials object
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
auth_req = Request()
credentials.refresh(auth_req)

# File to store history
HISTORY_FILE = 'history.json'

# Ensure history file exists 
if not os.path.exists(HISTORY_FILE) or os.stat(HISTORY_FILE).st_size == 0:
    with open(HISTORY_FILE, 'w') as f:
        json.dump([], f)

def load_history():
    with open(HISTORY_FILE, 'r') as f:
        return json.load(f)

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

def index_url(url, credentials):
    endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {credentials.token}"
    }
    payload = {
        "url": url,
        "type": "URL_UPDATED"
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        return True, f"Successfully indexed: {url}"
    else:
        return False, f"Failed to index: {url} - {response.status_code} - {response.text}"

@app.route('/')
def index():
    history = load_history()
    # Get the date today
    today_date = datetime.now().strftime("%Y-%m-%d")
    # Group history by date
    history_by_date = {}
    for entry in history:
        url, success, message, date = entry
        if date not in history_by_date:
            history_by_date[date] = []
        history_by_date[date].append((url, success, message))
    return render_template('index.html', history_by_date=history_by_date, today_date=today_date)

@app.route('/submit', methods=['POST'])
def submit():
    urls = request.form.get('urls')
    urls_list = urls.split('\n')
    results = []
    history = load_history()
    today_date = datetime.now().strftime("%Y-%m-%d")
    for url in urls_list:
        url = url.strip()
        if url:
            success, message = index_url(url, credentials)
            results.append((url, success, message))
            history.append((url, success, message, today_date))
    save_history(history)
    return render_template('result.html', results=results, today_date=today_date, history_by_date={today_date: results})

if __name__ == '__main__':
    app.run(debug=True)
