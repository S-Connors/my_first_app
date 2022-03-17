from rich import print
from rich.pretty import Pretty
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console
import re

# Create your rich console
con = Console()

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
        is_movable = is_movable

#create garden items
sunflower = Item("sunflower", "Beautiful yellow sunflower in bloom", True)
leaves = Item('leaves', 'Small green leaves. They smell nice', True)
rock = Item('rock', 'Grey rock about the size of a baseball', True)

#create kitchen items
chef = Item('chef', 'He is chopping vegtables with a very LARGE knife. He looks suprised and unhappy you are there.', False)
bones = Item('bones', 'Looks like leftover bones.',True)
apple = Item('apple', 'Red apple', True)

#create living room items
dog = Item('dog', 'Large black dog. He is sleeping but could wake up any moment. I do not think he would like you being there', False)
scrap_paper = Item('scrap of paper', 'A handwritten note with the numbers 487932', True)
book = Item('book','Looks like a book with a highlighted passage. Ninty seven animals animals live in the surrounding area. Only fourty three are harmless, the remaining fifty four are dangerous.', True)

#create front yard items
tree = Item('tree','An old oak tree overlooks the gate. It looks easy to climb', False)
electric_lock = Item('electric lock','A lock to the gate with numbers 0-9. A password is required.', False)

#create room - garden
garden = Room('Garden', 'You are in a large garden with high cedar fencing. In the flower bed you see sunflowers, leaves and rocks. To the north is an open door to a house.')
garden.items.append(sunflower)
garden.items.append(leaves)
garden.items.append(rock)

#create room - kitchen
kitchen =Room('Kitchen','You are in a large kitchen. A chef preparing dinner. Beside him are bones and an apple. To the east you see another door. To the south is the garden.')
kitchen.items.append(chef)
kitchen.items.append(bones)
kitchen.items.append(apple)

#create room - living Room
living_room = Room('Living Room','You are in a living room. There are locked glass windows to the east. A large dog is sleeping by a door to the north. To the west is the kitchen.')
living_room.items.append(dog)
living_room.items.append(scrap_paper)
living_room.items.append(book)

#create room - front yard
front_yard = Room('Front Yard', 'You are in the front yard. A large gate with an electric lock blocks the street. Beside the gate is a tree. To the south is the living room.')
front_yard.items.append(tree)
front_yard.items.append(electric_lock)

#create exits
garden.exits['n'] = kitchen
kitchen.exits['s'] = garden
kitchen.exits['e'] = living_room
living_room.exits['n'] = front_yard
living_room.exits['w'] = kitchen
front_yard.exits['s'] = living_room

# Get the name of your user
name = Prompt.ask(
    "Please enter your name",
    # choices=["Stephanie", "Christian", "Jen"],
    default="Player"
)

#ask player if they want to play
ans = input(f"Hello {name}. Would you like to try my game? y/n ")
if re.match("n|N", ans):
    print("Come back when your ready")
else:
    print("Let's see if you can escape!")

#make  instructions
instructions = ("""You can move in 4 directions: n, s, e, w
You can interact with items: get, drop, examine, climb""")

panel = Panel(instructions, title="Instructions")
con.print(panel, style="bold green")

#create player
player = Player(name, garden)
