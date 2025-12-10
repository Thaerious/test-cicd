"""Console script for test_cicd."""

import typer
from rich.console import Console

from test_cicd import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for test_cicd."""
    console.print("Replace this message by putting your code into "
               "test_cicd.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
