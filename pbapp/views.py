from flask import Flask, render_template, request, jsonify
import datetime
from lib_exp import load_parser, quest_geocode, quest_wiki
from pbapp.libs.message import Message

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def index():
    date = datetime.datetime.now()
    h = date.hour
    m = date.minute
    s = date.second
    message_home = Message()
    message = message_home.message_home()

    return render_template('index.html', message=message, heure=h, minute=m, second=s)


@app.route('/quest', methods=['POST'])
def quest():
    result = request.form
    q = result["quest"]
    parser = load_parser(q)
    print(parser)
    nb = parser.count(" ")
    if nb <= 1:
        message_grandpy = Message()
        message_grandpy.message_geocode()
        message = message_grandpy.message_wikimedia()

        geocode = quest_geocode(parser)
        wikimedia = quest_wiki(parser)

        return jsonify({'quest': q, 'message': message, 'parser': parser, 'geo': geocode, 'wiki': wikimedia})

    else:
        message_error = Message()
        message = message_error.message_error()
        error = 1

        return jsonify({'quest': q, 'message': message, 'error': error})


if __name__ == "__main__":
    app.run(debug=True)
