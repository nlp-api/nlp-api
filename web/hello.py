from flask import Flask, request
from nltk.corpus import opinion_lexicon
from nltk.tokenize import treebank
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        print(demo_liu_hu_lexicon('This is a nice car.'))
        print(demo_liu_hu_lexicon('This is a terrible car.'))
        print(demo_vader_instance('This is a nice car.'))
        print(demo_vader_instance('This is a terrible car.'))
        return 'print'


def demo_liu_hu_lexicon(sentence):
    """
    Basic example of sentiment classification using Liu and Hu opinion lexicon.
    This function simply counts the number of positive, negative and neutral words
    in the sentence and classifies it depending on which polarity is more represented.
    Words that do not appear in the lexicon are considered as neutral.

    :param sentence: a sentence whose polarity has to be classified.
    :param plot: if True, plot a visual representation of the sentence polarity.
    """

    tokenizer = treebank.TreebankWordTokenizer()
    pos_words = 0
    neg_words = 0
    tokenized_sent = [word.lower() for word in tokenizer.tokenize(sentence)]

    x = list(range(len(tokenized_sent))) # x axis for the plot
    y = []

    for word in tokenized_sent:
        if word in opinion_lexicon.positive():
            pos_words += 1
            y.append(1) # positive
        elif word in opinion_lexicon.negative():
            neg_words += 1
            y.append(-1) # negative
        else:
            y.append(0) # neutral

    if pos_words > neg_words:
        print('Positive')
    elif pos_words < neg_words:
        print('Negative')
    elif pos_words == neg_words:
        print('Neutral')

def demo_vader_instance(text):
    """
    Output polarity scores for a text using Vader approach.

    :param text: a text whose polarity has to be evaluated.
    """
    vader_analyzer = SentimentIntensityAnalyzer()
    print(vader_analyzer.polarity_scores(text))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
