class Room():
    def __init__(self, name, discription):
        self.name = name
        self.discription = discription
        self.exits = {}
        self.items = []

class Player():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

class Item():
    def __init__(self, name, description, is_movable):
        self.name = name
        self.description = description
        self.is_movable = is_movable
        self.inventory = []
