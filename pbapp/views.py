from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def index():
    date = datetime.datetime.now()
    h = date.hour
    m = date.minute
    s = date.second
    return render_template('index.html', heure=h, minute=m, second=s)


@app.route('/quest', methods=['POST'])
def quest():
    result = request.form
    r = result["quest"]
    return render_template('index.html', quest=r)


if __name__ == "__main__":
    app.run(debug=True)


