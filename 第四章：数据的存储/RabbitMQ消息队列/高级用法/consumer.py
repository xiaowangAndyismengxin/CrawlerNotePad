import pika

QUEUE_NAME = 'crawler'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# channel.queue_declare(queue=QUEUE_NAME)


while True:
    input()
    method_frame, header, body = channel.basic_get(
        queue=QUEUE_NAME,
        auto_ack=True  # 是否自动确认
    )

    print(type(method_frame))
    print(method_frame)
    print(type(header))
    print(header)
    print(type(body))
    print(body)
    if body:
        print(f'Get: {body}')
