import requests

def tell_joke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single&lang=en"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json().get("joke", "No joke available.")
        return joke
    return "Sorry, I couldn't fetch a joke right now."
