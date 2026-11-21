import re

import typer
import requests
import json

app = typer.Typer()
BASE_URL = "http://localhost:8000"

def print_requests(response):
    try:
        print(f"Status Code: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
    except ValueError:
        print(f"Status Code: {response.status_code}")
        print(response.text)

@app.command()
def get_book(isbn: str, min_year :int = typer.Option(None, "--min-year", help="Min publish year")):
    """Fetch book details by ISBN"""
    try:
        response = requests.get(f"{BASE_URL}/book/{isbn}")
        print_requests(response)
        if min_year is not None:
            data = response.json()
            book = data.get("book", data)
            match = re.search(r"(\d{4})", book.get("publish_date", ""))
            if match and int(match.group(1)) < min_year:
                typer.echo(f"Book publish year is less than {min_year}")
            
    except requests.RequestException as e:
        typer.echo(f"Error: Failed to connect to server - {str(e)}")

@app.command()
def search_book(title:str):
    """Search for books by title"""
    try:
        response = requests.get(f"{BASE_URL}/book/search/{title}")
        print_requests(response)
    except requests.RequestException as e:
        typer.echo(f"Error: Failed to connect to server - {str(e)}")

@app.command()
def bulk_books(isbn:list[str]):
    """Search for books by ISBN in bulk"""
    try:
        response = requests.post(f"{BASE_URL}/books/bulk/", json=isbn)
        print_requests(response)
    except requests.RequestException as e:
        typer.echo(f"Error: Failed to connect to server - {str(e)}")



if __name__ == "__main__":
    app()