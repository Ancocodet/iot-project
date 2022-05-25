import json


class Config:

    data = None

    broker = None
    door = None

    def __init__(self, path):
        with open(path, 'r') as f:
            self.data = json.load(f)
        if self.data is not None:
            self.broker = self.data['broker']
            self.door = self.data['door']
