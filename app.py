from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    """DOCSTRINGS NEEDED"""

    return render_template('index.html')