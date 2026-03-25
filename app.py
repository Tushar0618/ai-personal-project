from flask import Flask
import random
import time
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def home():
    if random.random() > 0.8:
        logging.error("Random failure occurred!")
        return "Error!", 500
    logging.info("Request successful")
    return "Hello DevOps + AI 🚀"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

