import pika
import pika.credentials


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        credentials=pika.credentials.PlainCredentials(
            username='root',
            password='root'
        )
    )
)
channel = connection.channel()
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

connection.close()
