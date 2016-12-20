# streamteam2
CLI helper for streaming Emotiv EEG data to pubnub or rabbitmq

## System level prereqs
* Install hidapi http://www.signal11.us/oss/hidapi/
* Install pyhidapi https://github.com/NF6X/pyhidapi
* `sudo apt install virtualenv`
## Application level prereqs
* Create and source the venv, and install the prereqs
```bash
git clone git@github.com:jamesbeedy/streamteam2.git
cd streamteam2
virtualenv -p python3 .stream
source .stream/bin/activate
pip install -r requirements.txt
```

## RabbitMQ Config
Rabbitmq configs must be passed into the application by specifying a yaml file with rabbit creds defined.
```yaml
#rabbit.yaml
username: jujuclient
password: 'somelongpassword'
host: 'rabbit-host'
port: 'rabbit-port'
vhost: 'rabbit-vhost'
queue: 'rabbit-queue'
exchange: 'rabbit-exchange'
```

## Run Pub/Sub
* Use the same config file to publish or subscribe
```bash
# to publish from an emotiv eeg
./main.py --publish configs rabbit.yaml
# to subscribe to the rabbit queue
./main.py --subscrribe configs rabbit.yaml
```

# Status: WIP



#### Copyright
* James Beedy (c) 2016 <jamesbeedy@gmail.com>
