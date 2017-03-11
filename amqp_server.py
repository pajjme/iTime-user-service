import pika

class AmqpServer:

    def __init__(self,server,request_queue,procedure):
        
        self.procedure = procedure

        self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=server))

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue = request_queue)
        
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(self.on_request,queue=request_queue)
    
    #Call this method to start accepting incoming RPC requests
    def start(self):
        print("Wating for RPC requests ...")
        self.channel.start_consuming()

    #Callback method that will be called on eache RPC request

    def on_request(self,channel,method,properties,body):
        result = self.procedure(body)

        if result == None:
             result = "{msg:empty}"
         
        channel.basic_publish(exchange='',
            routing_key= properties.reply_to,
            properties=pika.BasicProperties(
                correlation_id = properties.correlation_id),
            body = str(result) 
            )

        channel.basic_ack(delivery_tag = method.delivery_tag)

