import requests

def interesting_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("text", "Couldn't fetch a fact right now.")
    return "Sorry, no facts are available at the moment."
