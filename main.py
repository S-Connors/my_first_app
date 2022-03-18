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
        self.is_movable = is_movable
        self.inventory = []

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
paper = Item('paper', 'A handwritten note with the numbers 487932', True)
book = Item('book','Looks like a book with a highlighted passage. Ninty seven animals animals live in the surrounding area. Only fourty three are harmless, the remaining fifty four are dangerous.', True)

#create front yard items
tree = Item('tree','An old oak tree overlooks the gate. It looks easy to climb', False)
lock = Item('lock','A lock to the gate with numbers 0-9. A password is required.', False)
gate = Item('gate',"A large impenetrable gate.",False)

#create room - garden
garden = Room('Garden', 'You are in a large garden with high cedar fencing. In the flower bed you see sunflowers, leaves and rocks. To the north is an open door to a house.')
garden.items.append(sunflower)
garden.items.append(leaves)
garden.items.append(rock)

#create room - kitchen
kitchen =Room('Kitchen','You are in a large kitchen. A chef preparing dinner. Beside him are bones and an apple. To the east you see another door.')
kitchen.items.append(chef)
kitchen.items.append(bones)
kitchen.items.append(apple)

#create room - living Room
living_room = Room('Living Room','You are in a living room. There are locked glass windows to the east. A large dog is sleeping by a door to the north.')
living_room.items.append(dog)
living_room.items.append(paper)
living_room.items.append(book)

#create room - front yard
front_yard = Room('Front Yard', 'You are in the front yard. A large gate lock blocks your escape to the street.')
front_yard.items.append(tree)
front_yard.items.append(lock)
front_yard.items.append(gate)

#create exits
garden.exits['north'] = kitchen
kitchen.exits['south'] = garden
kitchen.exits['east'] = living_room
living_room.exits['north'] = front_yard
living_room.exits['west'] = kitchen
front_yard.exits['south'] = living_room

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
instructions = ("""You can move in 4 directions: north, south, east, west
You can interact: get, drop, examine, climb, give
You can check your inventory: inv""")

panel = Panel(instructions, title="Instructions")
con.print(panel, style="bold green")

#create player
player = Player(name, garden)

#print info
while True:
    print('')
    print(player.location.name)
    print(player.location.discription)
    print('Here are the exits:')
    for exit in player.location.exits:
        print(exit)

    print('Here are the things around you:')
    for item in player.location.items:
        print(item.name)

    #get command
    command = input("""What would you like to do?
    >""")

    words = command.split()
    if len(words) > 0:
        verb = words[0]
    if len(words) >1:
        noun = words[1]
    if len(words) >2:
        w_three = words[2]

    #examine
    if verb == 'examine':
        for item in player.location.items:
            if item.name == lock:
                code = input("Enter code ")
                if code == '974354':
                    print('Your code opened the gate! You are free!')
                    quit()
                else:
                    print('Your code does not work')
        for item in player.location.items:
            if item.name == noun:
                print(item.description)
        for item in player.inventory:
            if item.name == noun:
                print(item.description)

    #get
    if verb == 'get':
        for item in player.location.items:
            if item.name == noun:
                if item.is_movable:
                    print(f"{item.name} is added to your inventory")
                    player.location.items.remove(item)
                    player.inventory.append(item)
                else:
                    print("Sorry, you can't move that")

    #climb - need editing
    if verb == 'climb':
        for item in player.location.items:
            if item.name == 'tree':
                if apple in player.inventory:
                    print("A bird flew out of the tree and attacked you. You gave him your apple and ran away.")
                    player.inventory.remove(apple)
                else:
                    print("You tried climbing the tree. Unfortunatly you fell out and broke your ankle. Game over. ")
                    quit()
            if item.name == 'gate':
                print("You tried climbing the gate, but you fell down and broke your ankle. Game over.")
                quit()
            else:
                print("You can not climb this")

    #drop
    if verb == 'drop':
        for item in player.inventory:
            if item.name == noun:
                print(f"{item.name} has been removed from your inventory")
                player.inventory.remove(item)
                player.location.items.append(item)

    #give
    if verb == 'give':
        for item in player.inventory:
            if item.name == w_three:
                for object in player.location.items:
                    if object.name == noun:
                        print(f"You gave {item.name} to {object.name}")
                        player.inventory.remove(item)
                        object.inventory.append(item)

    #inventory
    if verb == 'inventory':
        print("You have the following: ")
        for item in player.inventory:
            print(item.name)

    #move - check to see if works
    if verb == 'exit':
        if noun in player.location.exits:
            player.location = player.location.exits[noun]
            print(f"You go {noun} and enter the {player.location.name}.")
        else:
            print("You can not go that way")

    #kitchen specific
    if player.location == kitchen:
        if verb == 'exit' and leaves not in chef.inventory and noun == 'east':
            print("The chef caught you. He threw you back outside and locked the door. Game over")
            quit()
        if leaves in chef.inventory:
            print('The green leaves you gave the chef turned out to be oregano. He is engrossed in adding it to his dinner.')

    #living room specific
    if player.location == living_room:
        if verb == 'exit' and noun == 'north' and bones not in dog.inventory:
            print("You woke up the dog. Suprised by your intrusion he bit you! Game over.")
            quit()
        if bones in dog.inventory:
            print("The dog happily accepted your gift and is munching on the bones.")

    #front yard specific
