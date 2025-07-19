import pika

QUEUE_NAME = "crawler"
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)


def callback(ch, method, properties, body):
    print(
        "ch: ",
        type(ch),
        "\n",
        ch,
        "\n",
        "method: ",
        type(method),
        "\n",
        method,
        "\n",
        "properties: ",
        type(properties),
        "\n",
        properties,
        "\n",
        "body: ",
        type(body),
        "\n",
        body,
    )


channel.basic_consume(
    queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True  # 是否自动确认
)

channel.start_consuming()
