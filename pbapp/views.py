from flask import Flask, render_template, request, jsonify
import datetime
from lib_exp import load_parser, quest_geocode, quest_wiki


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
    q = result["quest"]
    parser = load_parser(q)
    geocode = quest_geocode(parser)
    wikimedia = quest_wiki(parser)
    message = geocode

    return render_template('index.html', jsonify={"quest": q, "parser": parser, "geo": geocode, "wiki": wikimedia})


if __name__ == "__main__":
    app.run(debug=True)


