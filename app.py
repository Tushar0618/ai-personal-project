from flask import Flask
import random
import logging
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total Requests')
ERROR_COUNT = Counter('app_errors_total', 'Total Errors')

logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    if random.random() > 0.8:
        ERROR_COUNT.inc()
        logging.error("Random failure occurred!")
        return "Error!", 500
    logging.info("Request successful")
    return "Hello DevOps + AI 🚀"

if __name__ == "__main__":
    start_http_server(8000)  # metrics port
    app.run(host='0.0.0.0', port=5000)