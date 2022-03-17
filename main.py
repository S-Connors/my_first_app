from rich import print
from rich.pretty import Pretty
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console

# Create your rich console
con = Console()


# Get the name of your user
name = Prompt.ask(
    "Please enter your name",
    # choices=["Stephanie", "Christian", "Jen"],
    default="Stephanie"
)

# Now print
pretty = Pretty(f"Hello {name}")
panel = Panel(pretty, title="Welcome 🎉", subtitle="Thank you!")
con.print(panel, style="bold green")

con.print("Would you like to play a game?", style="red")
