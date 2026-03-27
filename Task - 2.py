from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.text import Text
import time

console = Console()

console.print("[bold cyan]Initializing Sourcesys System...[/bold cyan]")
for _ in track(range(30), description="Loading..."):
    time.sleep(0.05)

time.sleep(0.5)
console.clear()

def type_writer(text, delay=0.03):
    for char in text:
        console.print(char, end="")
        time.sleep(delay)
    console.print()

title = Text("SOURCESYS", style="bold blue")
console.print(Panel(title, expand=False))

type_writer("\nHi, I'm Hitesh Kumar S")
type_writer("Full Stack Developer Intern at Sourcesys\n")

info = """
[bold]Name:[/bold] Hitesh Kumar S
[bold]Role:[/bold] Full Stack Developer Intern
[bold]Company:[/bold] Sourcesys

[bold]Tagline:[/bold]
Building and learning modern web technologies
"""

console.print(Panel(info, title="Profile", border_style="cyan"))

skills = """
• HTML  
• CSS  
• JavaScript  
• Python  
• SQL  
"""

console.print(Panel(skills, title="Skills", border_style="green"))
console.print("\n[bold yellow]Launching Developer Mode...[/bold yellow]")
for i in range(0, 101, 25):
    console.print(f"[green]Progress: {i}%[/green]")
    time.sleep(0.1)

console.print("\n[bold green]✔ System Ready! Welcome to Sourcesys [/bold green]")