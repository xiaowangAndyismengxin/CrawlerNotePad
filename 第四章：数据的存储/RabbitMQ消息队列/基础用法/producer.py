import pika

QUEUE_NAME = "crawler"
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)
print(type(channel))

channel.basic_publish(exchange="", routing_key=QUEUE_NAME, body="Hello World!")
