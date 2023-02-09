import glob
import os
from typing import Optional
from Utilities.Utilities import Utilities

import json

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
    # TODO: Pick up here for loading owner data
    owner_data = json.load('owner_data.json')
    for owner in owner_data:
        print(owner)
    print('Starting the Ingest')
    # Utilities.execute(data, 'data_source_name')
    owner_data.close()
    return None

if __name__ == '__main__':
    app()
