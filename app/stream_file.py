import json
import pandas as pd
import logging
from kafka import KafkaProducer
from redis_cache import get_last_processed_line, set_last_processed_line


producer = KafkaProducer(
    bootstrap_servers=['kafka:29092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def process_csv_file(file_path, kafka_topic, batch_size=1):
    last_processed_line = get_last_processed_line(kafka_topic)
    chunksize = batch_size

    for chunk in pd.read_csv(file_path, chunksize=chunksize, skiprows=range(0, last_processed_line)):

        for _, row in chunk.iterrows():
            data_record = row.to_dict()
            producer.send(kafka_topic, value=data_record).add_callback(
                lambda record_metadata: print(f"Sent: {record_metadata.topic} [{record_metadata.partition}] @ {record_metadata.offset}")
            ).add_errback(
                lambda exc: print(f"Failed to send message: {exc}")
            )
            producer.flush()

        last_line_number = chunk.index[-1] + 1
        set_last_processed_line(kafka_topic, last_line_number)
