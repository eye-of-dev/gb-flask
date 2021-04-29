from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def hello_gb():
    if request.method == 'POST':
        return 'This is POST request', 200
    else:
        return 'This is GET request', 200
