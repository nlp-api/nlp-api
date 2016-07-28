from flask import Flask, request, jsonify
from .sentiment import Sentiment

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'API'

@app.route('/api/sentiment', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return jsonify(text='This is how you should format your POST data.')
    if request.method == 'POST':
        try:
            f = request.get_json()
        except Exception as e:
            # Should log this error maybe?
            print(e)
            return not_acceptable()
        else:
            for text in f:
                print(f[text])
                return jsonify(Sentiment.demo_vader_instance(f[text]))


@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.errorhandler(406)
def not_acceptable(error=None):
    message = {
            'status': 406,
            'message': 'Could not parse json, check formatting: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 406

    return resp


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
