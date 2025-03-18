import pika
import json
import time
import concurrent.futures
from src.config import RABBITMQ_HOST, RABBITMQ_PORT
from src.program import ScraperService
from src.driverPool import DriverPool

driver_pool = DriverPool(pool_size=10)
# Create a thread pool for running the searches concurrently.
executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)  # Adjust as needed

def callback(ch, method, properties, body):
    try:
        search_terms = json.loads(body.decode('utf-8'))

        if isinstance(search_terms, list):
            for search_term in search_terms:
                print("Received search term:", search_term)
                executor.submit(ScraperService.search, search_term, driver_pool)
        else:
            print("Received non-list message:", search_terms)

    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    except Exception as e:
        print("Error processing message:", e)
    finally:
        ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consumer():
    time.sleep(15)
    connection_params = pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    queue_name = "product_queue"
    channel.queue_declare(queue=queue_name, durable=False)
    channel.basic_qos(prefetch_count=10)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)
    print(f"Waiting for messages on queue '{queue_name}' (RabbitMQ host: {RABBITMQ_HOST})...")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Stopping consumer...")
        channel.stop_consuming()
    connection.close()

if __name__ == "__main__":
    try:
        start_consumer()
    finally:
        executor.shutdown(wait=False)
        driver_pool.shutdown()