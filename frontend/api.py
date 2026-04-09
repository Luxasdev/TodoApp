import requests

BASE_URL = "http://127.0.0.1:8000"

def get_todos():
    return requests.get(f"{BASE_URL}/todos").json()

def add_todo(title):
    requests.post(f"{BASE_URL}/todos", json={"title": title})