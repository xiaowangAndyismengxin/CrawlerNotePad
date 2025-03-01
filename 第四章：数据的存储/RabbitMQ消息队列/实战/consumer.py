import pika
import requests
import pickle

QUEUE_NAME = 'crawler'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

session = requests.Session()
while True:
    method_frame, header, body = channel.basic_get(
        queue=QUEUE_NAME,
        auto_ack=True  # 是否自动确认
    )
    if body:
        req = pickle.loads(body)
        prepared = session.prepare_request(req)
        resp = session.send(prepared)
        print(resp.status_code)
        continue
    break
