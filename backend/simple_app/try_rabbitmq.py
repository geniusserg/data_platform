import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=pika.credentials.PlainCredentials(username='root', password='root')))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()