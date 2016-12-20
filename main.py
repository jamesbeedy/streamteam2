#!/usr/bin/env python3
import yaml, json, argparse, time
from argparse import ArgumentParser
from emokit.emotiv import Emotiv
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
    rabbit = Rabbit(yaml_args)

    if args.sub:
        rabbit.subscribe()

    if args.pub:
        with Emotiv(display_output=True, verbose=True, write=True) as headset:
            while True:
                packet = headset.dequeue()
                if packet is not None:
                    rabbit.publish(json.dumps(raw_data_all(packet)))
                time.sleep(0.001)
