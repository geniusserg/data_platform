def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


import pika
import pika.credentials

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=pika.credentials.PlainCredentials(username='root', password='root')))
channel = connection.channel()

import time

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

connection.close()
