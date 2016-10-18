from flask import Flask,jsonify
import random
app = Flask(__name__)


from quotes import motivational_qoutes
from quotes import funny_qoutes


@app.route('/')
def hello_world():
    return 'Api is working! Happy Coding'

@app.route('/api/motivational')
def serve_motivational_quote():
    quotes=motivational_qoutes()
    nr_of_quotes= len(quotes)
    selected_quote= quotes[random.randint(0,nr_of_quotes-1)]
    return jsonify(selected_quote)


@app.route('/api/funny')
def serve_funny_quote():
    quotes = funny_qoutes()
    nr_of_quotes = len(quotes)
    selected_quote = quotes[random.randint(0, nr_of_quotes - 1)]
    return jsonify(selected_quote)


if __name__ == '__main__':
    app.run(debug=True)
