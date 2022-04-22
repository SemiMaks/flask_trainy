from collections import namedtuple

from flask import Flask, render_template

app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/main")
def main():
    return render_template('main.html', message=messages)


if __name__ == "__main__":
    app.run(debug=True)
