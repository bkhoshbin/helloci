from flask import Flask


app = Flask(__name__)

from prometheus_client import Counter, Summary

# Initialize request counters and processing time summaries
REQUEST_COUNT = Counter('request_count', 'The number of requests')
REQUEST_TIME = Summary('request_processing_seconds', 'The time spent processing requests')

@app.route("/add/<int:a>/<int:b>")
@REQUEST_TIME.time()
def add(a, b):
    REQUEST_COUNT.inc()
    return addNumbers(a, b)


@app.route("/multiply/<int:a>/<int:b>")
@REQUEST_TIME.time()
def multiply(a, b):
    REQUEST_COUNT.inc()
    return multiplyNumbers(a, b)

def multiplyNumbers(a, b):
    return str(a * b)

def addNumbers(a, b):
    return str(a + b)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World6!'



if __name__ == '__main__':
    app.run()
