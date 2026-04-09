import requests

BASE_URL = "https://todo-app.onrender.com"

def get_todos():
    response = requests.get(f"{BASE_URL}/todos")
    print(response.status_code, response.text)
    return response.json()

def add_todo(title):
    requests.post(f"{BASE_URL}/todos", json={"title": title})