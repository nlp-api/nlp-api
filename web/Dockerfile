FROM micktwomey/python3.4:latest
MAINTAINER Nick Roberts "nick.roberts.127.0.0.1@gmail.com"
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN python3.4 -m nltk.downloader opinion_lexicon vader_lexicon
ENTRYPOINT ["python3.4"]
CMD ["api.py"]
