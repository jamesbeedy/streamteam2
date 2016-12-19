# streamteam2
CLI helper for streaming Emotiv EEG data to pubnub or rabbitmq


RabbitMQ Config
Rabbitmq configs must be passed into the application by specifying a yaml file with rabbit creds defined.
'''yaml
username: jujuclient
password: 'somelongpassword'
host: 'rabbit-host'
port: 'rabbit-port'
vhost: 'rabbit-vhost'
queue: 'rabbit-queue'
exchange: 'rabbit-exchange'
'''
