from flask import Flask, request
from sentiment import Sentiment

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'API'

@app.route('/api/sentiment', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        print(Sentiment.demo_liu_hu_lexicon('This is a nice car.'))
        print(Sentiment.demo_liu_hu_lexicon('This is a terrible car.'))
        print(Sentiment.demo_vader_instance('This is a nice car.'))
        print(Sentiment.demo_vader_instance('This is a terrible car.'))
        return 'print'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
