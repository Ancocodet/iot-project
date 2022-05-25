import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

from utils.config import Config
from utils.client_handler import ClientHandler

config = Config('config/config.json')
client = ClientHandler(config=config.broker)

reader = SimpleMFRC522()


def validate_id(id):
    return id in config.door['allowed']


try:
    while True:
        id, text = reader.read()
        if validate_id(id):
            client.publish_status()
        time.sleep(config['timeout'])
except KeyboardInterrupt:
    client.disconnect()
finally:
    GPIO.cleanup()
