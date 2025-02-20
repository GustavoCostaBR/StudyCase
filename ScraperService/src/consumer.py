import pika
import os
import time

def start_consumer():
    rabbitmq_host = os.environ.get('RABBITMQ_HOST') or 'localhost' # Default to localhost for local testing
    connection_params = pika.ConnectionParameters(host=rabbitmq_host)

    try:
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()
        channel.queue_declare(queue='test_queue', durable=False, exclusive=False, auto_delete=False)
        print(" [*] Waiting for messages. To exit press CTRL+C")

        def callback(ch, method, properties, body):
            print(f" [x] Received {body.decode()}")

        channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError as e:
        print(f"Connection Error: {e}")
        time.sleep(5)  # Wait and retry


if __name__ == '__main__':
    while True: # Retry loop
        try:
            start_consumer()
            break # Exit loop if consumer starts successfully
        except Exception as e:
            print(f"Error starting consumer: {e}")
            time.sleep(5) # Wait before retrying






































# import pika
# import json
# import os
# from src.config import RABBITMQ_HOST, RABBITMQ_PORT

# def callback(ch, method, properties, body):
#     try:
#         # Assume the message is JSON encoded.
#         message = json.loads(body)
#         print("Received message:", message)
#     except Exception as e:
#         print("Error processing message:", e)
#     finally:
#         ch.basic_ack(delivery_tag=method.delivery_tag)

# def start_consumer():
#     # Use the connection parameters from config.
#     connection_params = pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT)
#     connection = pika.BlockingConnection(connection_params)
#     channel = connection.channel()

#     # Declare the queue. Make sure the queue name matches what your API publishes.
#     queue_name = "product_queue"
#     channel.queue_declare(queue=queue_name, durable=False)

#     # Set up basic consumption on the queue.
#     channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

#     print(f"Waiting for messages on queue '{queue_name}' (RabbitMQ host: {RABBITMQ_HOST})...")
#     try:
#         channel.start_consuming()
#     except KeyboardInterrupt:
#         print("Stopping consumer...")
#         channel.stop_consuming()
#     connection.close()

# if __name__ == "__main__":
#     start_consumer()
