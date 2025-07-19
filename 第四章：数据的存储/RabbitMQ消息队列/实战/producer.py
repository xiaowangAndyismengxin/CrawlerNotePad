import requests
import pika
import pickle

MAX_PRIORITY = 100
QUEUE_NAME = "crawler"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
# rabbitmqctl delete_queue crawler
channel.queue_delete(queue=QUEUE_NAME)
channel.queue_declare(queue=QUEUE_NAME)


def get_requests(url="https://ssr1.scrape.center", count=10):
    return [requests.Request("GET", url) for _ in range(count)]


for request in get_requests():
    data = pickle.dumps(request)
    channel.basic_publish(exchange="", routing_key=QUEUE_NAME, body=data)
    print(f"produced data:{data}")
