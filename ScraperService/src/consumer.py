import pika
import json
import time
import os
from src.config import RABBITMQ_HOST, RABBITMQ_PORT

def callback(ch, method, properties, body):
    try:
        # Assume the message is JSON encoded.
        message = json.loads(body)
        print("Received message:", message)
    except Exception as e:
        print("Error processing message:", e)
    finally:
        ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consumer():
    # Use the connection parameters from config.
    time.sleep(20)
    connection_params = pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Declare the queue. Make sure the queue name matches what your API publishes.
    queue_name = "product_queue"
    channel.queue_declare(queue=queue_name, durable=False)

    # Set up basic consumption on the queue.
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

    print(f"Waiting for messages on queue '{queue_name}' (RabbitMQ host: {RABBITMQ_HOST})...")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Stopping consumer...")
        channel.stop_consuming()
    connection.close()

if __name__ == "__main__":
    start_consumer()
