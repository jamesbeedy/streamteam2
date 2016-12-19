import pika


class Rabbit:
    def __init__(self, args):
        self.rabbit_user = args['username']
        self.rabbit_pass = args['password']
        self.rabbit_host = args['host']
        self.rabbit_vhost = args['vhost']
        self.rabbit_port = args['port']
        self.rabbit_queue = args['queue']
        self.rabbit_exchange = args['exchange']
        self.rabbit_routing_key = args['routing-key']

        self.creds = pika.PlainCredentials('%s' % self.rabbit_user, '%s' % self.rabbit_pass)


    def publish(self, msg):
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(
                                                host='%s' % self.rabbit_host,
                                                port=self.rabbit_port,
                                                virtual_host='%s' % self.rabbit_vhost,
                                                credentials=self.creds))



        self.channel = self.conn.channel()

        self.channel.queue_declare(queue=self.rabbit_queue)
        self.channel.basic_publish(exchange=self.rabbit_exchange,
                                   routing_key=self.rabbit_routing_key,
                                   body=msg)

    def subscribe(self):
        def callback(ch, method, properties, body):
            print(str(body.decode()))
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(
                                                host='%s' % self.rabbit_host,
                                                port=self.rabbit_port,
                                                virtual_host='%s' % self.rabbit_vhost,
                                                credentials=self.creds))



        self.channel = self.conn.channel()

        self.channel.queue_declare(queue=self.rabbit_queue)
        self.channel.basic_consume(callback, queue=self.rabbit_queue,
                                   no_ack=True)
        self.channel.start_sonsuming()

    def close(self):
        self.conn.close()
