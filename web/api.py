from flask import Flask, request, jsonify
import time
import datetime
from sentiment import Sentiment
from auth import Auth
from errors import Errors

timestamp = time.time()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'API'

@app.route('/api/sentiment', methods=['GET', 'POST'])
@Auth.auth_required
def api():
    if request.method == 'GET':
        return jsonify(text='This is how you should format your POST data.')
    if request.method == 'POST':
        try:
            f = request.get_json()
        except Exception as e:
            # Should log this error maybe?
            print(e)
            return Errors.bad_request()
        else:
            for text in f:
                print(datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))
                return jsonify(Sentiment.demo_vader_instance(f[text]))




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
