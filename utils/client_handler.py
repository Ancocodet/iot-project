import paho.mqtt.client as mqtt
import json

class ClientHandler:

    client = None
    config = None

    connected = False

    def __init__(self, config):
        self.config = config
        self.connect()

    def connect(self):
        self.client = mqtt.Client(self.config['clientname'])
        self.client.username_pw_set(self.config['username'], self.config['password'])
        self.client.on_connect = self.on_connect
        self.client.connect(self.config['hostname'], port=self.config['port'])
        self.client.loop_start()

    def disconnect(self):
        self.client(diconnect)
        self.client.loop_stop()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("connected to broker")
            self.connected = True
        else:
            print("Connected failed")

    def publish_status(self, topic, id, success):
        x = {
            "success": success,
            "id": id
        }
        self.client.publish("{}/request".format(topic), json.dumps(x), self.config['qos'])