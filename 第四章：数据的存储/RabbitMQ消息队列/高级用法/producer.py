import pika

MAX_PRIORITY = 100
QUEUE_NAME = 'crawler'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# rabbitmqctl delete_queue crawler
channel.queue_delete(queue=QUEUE_NAME)
channel.queue_declare(queue=QUEUE_NAME, arguments={
    'x-max-priority': MAX_PRIORITY
}, durable=True)
print(type(channel))

while True:
    data, priority = input('produce data: ').split()
    channel.basic_publish(
        exchange='',
        routing_key=QUEUE_NAME,
        properties=pika.BasicProperties(priority=int(priority),
                                        delivery_mode=2),
        body=data
    )
    print(f'produced data:{data}')
