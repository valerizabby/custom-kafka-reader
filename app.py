import threading

from flask import Flask, render_template, jsonify

from consumer import consume_latest_message
from json_processor import process_and_sort_json
from config import kafka_topic, kafka_servers

app = Flask(__name__)

processed_data = []

@app.route('/')
def index():
    """
    Renders the web page with the processed data.
    """
    return render_template('index.html', data=processed_data)

@app.route('/api/data', methods=['GET'])
def get_data():
    """
    Returns the processed data as JSON.
    """
    return jsonify(processed_data)

def kafka_worker():
    """
    Background worker to read Kafka messages and process them.
    """
    global processed_data
    while True:
        raw_message = consume_latest_message(kafka_topic, kafka_servers)
        if raw_message:
            processed_data = process_and_sort_json(raw_message)


if __name__ == "__main__":
    # Запускаем Kafka Worker в отдельном потоке
    threading.Thread(target=kafka_worker, daemon=True).start()

    # Запускаем Flask сервер
    app.run(host="0.0.0.0", port=4999, debug=True)