#!/usr/bin/env python3
import yaml, json, argparse, gevent
from argparse import ArgumentParser
from emokit import emotiv
from streamteam2.emotiv_headset import SENSOR_NAMES, raw_data_all
from streamteam2.rabbit import Rabbit


def create_parser():
    parser = ArgumentParser(
        description='Emotiv EEG PubSub Utility',
        prog='v0.0.1'
    )

    parser.add_argument(
        'configs',
        type=argparse.FileType('r')
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-p',
        '--publish',
        dest='pub',
        metavar='publish',
        help='publish'
    )
    group.add_argument(
        '-s',
        '--subscribe',
        dest='sub',
        metavar='subscribe',
        help = 'subscribe'
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s'
    )
    return parser



if __name__ == "__main__":

    parser = create_parser()
    args = parser.parse_args()
    yaml_args = yaml.load(args.configs)
    print(yaml_args)

    rabbit = Rabbit(yaml_args)

    headset = emotiv.Emotiv()
        
    if args.sub:
        try:
            while True:
                rabbit.subscribe()
        except KeyboardInterrupt:
            pass
        finally:
            pass

    if args.pub:
        gevent.spawn(headset.setup)
        gevent.sleep(1)
        try:
            while True:
                packet = headset.dequeue()
                rabbit.publish(json.dumps(raw_data_all(packet)))
                gevent.sleep(1)
        except KeyboardInterrupt:
            headset.close()
        finally:
            headset.close()
