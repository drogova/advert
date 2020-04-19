import json
import argparse
from advert.classes.advert import Advert


def test():
    with open('advert/data/test_adverts_json.txt', 'r') as f:
        for advert_json in f:
            advert_mapping = json.loads(advert_json)
            advert = Advert(advert_mapping)
            print(advert)
            print(advert.price)
            print(advert.class_)
            print(advert.location.address)
            print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='advert')
    parser.set_defaults(func=test)
    args = parser.parse_args()
    args.func()
