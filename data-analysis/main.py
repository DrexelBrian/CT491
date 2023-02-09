import glob
import os
from typing import Optional
import typer
from rich import print
from rich.console import Console
from rich.table import Table


# Consts and appwide declarations
app = typer.Typer()
console = Console()

@app.command()
def intro():
    table = Table(
        'Data Analysis of Pcap & other files')
    table.add_row(
        'In order to start the ETL process first identify the data source.')
    console.print(table)

@app.command()
def start(dataset: Optional[str] = None) -> None:
    """
        The main execution for handling all the different types of file formats.
        :params dataset, The optional CLI argument. This will be used when the user selects any of the
        returns None
    """
    print('Starting the Ingest')
    return None

if __name__ == '__main__':
    app()
