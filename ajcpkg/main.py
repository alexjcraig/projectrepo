"""begone pylint! Here is thy module docstring"""
from collections.abc import Iterable
import click
import requests


def openalex_institution(query):
    "query is a list of terms in the query, or a string."
    if isinstance(query, str):
        query = "+".join(query.split())

    # We assume it is an iterable of strings.
    elif isinstance(query, Iterable):
        query = "+".join(query)

    url = f"https://api.openalex.org/works/{query}"
    req = requests.get(url)
    data = req.json()

    return f'PY = {data["publication_year"]}\nTI = {data["title"]}\nJO = {data["host_venue"]["display_name"]}\nVL = {data["biblio"]["volume"]}\nIS = {data["biblio"]["issue"]}\nFP = {data["biblio"]["first_page"]}\nEP = {data["biblio"]["last_page"]}\nDO = {data["doi"]}'


@click.command(help="OpenAlex Institutions")
@click.argument("query", nargs=-1)
def main(query):
    """this will print the above function in the terminal"""
    print("\n".join(openalex_institution(query)))
