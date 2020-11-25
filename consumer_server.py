from kafka import KafkaConsumer

def consume_kafka_msg(topic):
    consumer = KafkaConsumer(
        bootstrap_servers="localhost:9092",
        auto_offset_reset='earliest'
    )

    consumer.subscribe([topic])

    for message in consumer:
        print(f"consumed message: {message}")

if __name__ == "__main__":
    consume_kafka_msg("com.udacity.sparkstreaming")