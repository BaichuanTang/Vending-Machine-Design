import os
import logging
import json
from configparser import ConfigParser


CONFIG_FILE = os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    'config.ini'
)

config_parser = ConfigParser()

config_parser.read(CONFIG_FILE)

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] [%(name)s] [%(levelname)s] (%(message)s)',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info('Loggers ready !')

# CHANGE THIS DICT if you have different class of emotions
EMOTION_MAP_PATH = os.path.join(
    os.path.dirname(__file__), 
    os.pardir, 
    'emotion_map.json'
)
with open(EMOTION_MAP_PATH) as json_file:
    EMOTION_MAP = json.load(json_file)
    logging.debug('Emotion Map: {}'.format(EMOTION_MAP))

ITEM_MAP_PATH = os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    'item_map.json'
)
with open(ITEM_MAP_PATH) as json_file:
    ITEM_MAP = json.load(json_file)
    logging.debug('Item Map: {}'.format(ITEM_MAP))