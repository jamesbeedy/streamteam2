# streamteam2
CLI helper for streaming Emotiv EEG data to pubnub or rabbitmq

To you this, you must source the venv
```bash
source .stream/bin/activate
```

RabbitMQ Config
Rabbitmq configs must be passed into the application by specifying a yaml file with rabbit creds defined.
```yaml
username: jujuclient
password: 'somelongpassword'
host: 'rabbit-host'
port: 'rabbit-port'
vhost: 'rabbit-vhost'
queue: 'rabbit-queue'
exchange: 'rabbit-exchange'
```
