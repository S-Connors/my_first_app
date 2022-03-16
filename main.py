from rich import print
from rich.pretty import Pretty
from rich.panel import Panel

name = "stephanie"
pretty = Pretty(f"Hello {name}")
panel = Panel(pretty)
print(panel)
