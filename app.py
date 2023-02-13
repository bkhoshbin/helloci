from flask import Flask
app = Flask(__name__)

import os
import time
from prometheus_client import Counter, Summary

# Initialize request counters and processing time summaries
REQUEST_COUNT = Counter('request_count', 'The number of requests')
REQUEST_TIME = Summary('request_processing_seconds', 'The time spent processing requests')

@app.route("/add/<int:a>/<int:b>")
@REQUEST_TIME.time()
def add(a, b):
    REQUEST_COUNT.inc()
    return str(a + b)

@app.route("/multiply/<int:a>/<int:b>")
@REQUEST_TIME.time()
def multiply(a, b):
    REQUEST_COUNT.inc()
    return str(a * b)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
