import pika

#Make connection to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#make queue to send msg on, this is idempotent
channel.queue_declare(queue='hello')

def callback(ch,method,prop,body):
    print("\t [x] Received %r" % body)

channel.basic_consume(callback,queue='hello',no_ack=True)

print('\t [*] Wating for messages. To exit press CTRL+C')
channel.start_consuming()
