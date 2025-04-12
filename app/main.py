# main.py
import json
import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():

    json_path = os.path.join(app.root_path, 'data', 'account.json')
    with open(json_path, 'r', encoding='utf-8') as file:
        accounts = json.load(file)
    
    return render_template('index.html', accounts=accounts)
