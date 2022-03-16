"""
This code was created by following this really cool medium article:
https://medium.com/nerd-for-tech/how-to-look-like-a-hacker-with-python-bd1a9116037f

Install the recs:
pip install pyfiglet rich


For proper documentation, read this bad boy: https://rich.readthedocs.io/en/stable/index.html

Explore fonts through this cool tool: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
"""
import pyfiglet
from rich.console import Console
from rich.console import Group
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt
from rich.progress import Progress,track

import os
import sys
import time
import socket


# --------------------------------------------

# Create your rich console
con = Console()


# A useful function to appear like you're thinking
def think(message='Initializing...', n=10, s=0.05):
    for i in track(range(n), message):
        time.sleep(s)

# --------------------------------------------

# Define your evil program

def web_hacking():

    # Initialize web hacking
    message = 'Initializing web hacking...'
    think(message)

    url = Prompt.ask('Enter website domain')

    # Message
    message = f'Gathering information on {url}'
    think(message, 50, 0.01)

    with Progress(refresh_per_second=100) as prog :
        exploiting = prog.add_task('Exploiting the website', total=100)
        enabling = prog.add_task('Enabling site wide access', total=225)
        inferring = prog.add_task('Running inference engine', total=60)
        decoding = prog.add_task('Cracking the passwords hashes', total=150)
        hide_trace = prog.add_task('Hiding security traces', total=110)
        dumping = prog.add_task('Dumping plain text passwords', total=300)


        while not prog.finished:
            prog.update(exploiting, advance=1)
            prog.update(enabling, advance=1)
            prog.update(inferring, advance=1)
            prog.update(decoding, advance=1)
            prog.update(hide_trace, advance=1)
            prog.update(dumping, advance=1)
            time.sleep(0.01)

    # Finally, print all the crazy stuff to make it look like something is happening
    start = time.time()
    for x in os.walk("/"):
        con.print(x, style="green")

        end = time.time()
        t = end - start
        # Stop after 10 seconds
        if t > 5:
            break

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    # Get schwifty with the final message
    # Finally, a message that you've finished
    my_banners = []
    message = 'WEB HACK COMPLETED'
    banner = pyfiglet.figlet_format(message, font='banner3-D')
    my_banners.append(banner)

    message = '****\n' + url + '\n****'
    banner = pyfiglet.figlet_format(url,font='Univers')
    my_banners.append(banner)

    message = 'IS FULLY COMPROMISED'
    banner = pyfiglet.figlet_format(message,font='banner3-D')
    my_banners.append(banner)

    # Print it
    con.print(*my_banners, style="bold green")




# --------------------------------------------

# Create a welcome banner with a welcome message
banner_message = socket.gethostname()
banner = pyfiglet.figlet_format(banner_message,font='banner3-D')
con.print(banner, style="bold green")

# Load
launch_message = 'Launching deep hacker probe.'
think(launch_message, 20)




# --------------------------------------------

hacker_choices = (
    'Web App Hacking',
    'Phishing Attack',
    'Social Engineering Kit',
    'MITM Attack',
    'WIFI Override'
    )

stuff = Group(*[Panel(x) for x in hacker_choices])
con.print(Panel(stuff),style="bold green")

# Choose one
choose_message = 'Choose a hack: \n(it doesn\'t matter which you choose, it\'ll default to web app hacking)\n'
answer = IntPrompt.ask(
    choose_message,
    choices=[str(i) for i in range(1, len(hacker_choices))]
    )

# Depending on your choice, launch that hacking program
web_hacking()
#
