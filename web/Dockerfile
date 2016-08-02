FROM python:3.4
ENV PYTHONUNBUFFERED 1
MAINTAINER Nick Roberts "nick.roberts.127.0.0.1@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m nltk.downloader opinion_lexicon vader_lexicon
ENTRYPOINT ["python"]
CMD ["api.py"]
