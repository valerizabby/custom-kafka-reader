from kafka import KafkaConsumer
import json


def consume_latest_message(topic, kafka_servers):

    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=kafka_servers,
        group_id=None,
        auto_offset_reset='latest',
        enable_auto_commit=False
    )

    for message in consumer:
        raw_bytes = message.value
        print(f"Сырые байты: {raw_bytes}")
        return message.value