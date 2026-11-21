# public_api_lab

This projec implements a FastAPI backend that fetches book data from the Open library API and a Typer-based Python client to interact with it.

## Setup
1. Create a virtual environment: 'python -m venv venv'
2. Activate it: 'source venv/bin/activate' (Windows: 'venv\Scripts\activate')
3. Install dependecies: 'pip install -r requirements.txt'

## Running the Server
cd server
python main.py

cd ..

cd client
python client.py get-book 9780142437247
python client.py search-title Love
python client.py get-bulk 9000000000 9000000001