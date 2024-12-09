# import requests

# def fetch_latest_news(api_key, category="general", country="in"):
#     """
#     Fetches the latest news headlines using the News API.
    
#     Parameters:
#         api_key (str): Your News API key.
#         category (str): Category of news (e.g., general, technology, sports).
#         country (str): Country code for news (e.g., us, in).

#     Returns:
#         list: A list of the top news headlines.
#     """
#     url = "https://newsapi.org/v2/everything?q=tesla&from=2024-10-27&sortBy=publishedAt&apiKey=a6753501654f4010be3e58481255fb80"
    
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         data = response.json()

#         if data["status"] == "ok" and data["totalResults"] > 0:
#             headlines = [article["title"] for article in data["articles"]]
#             return headlines
#         else:
#             return ["No news found at the moment."]
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching news: {e}")
#         return ["Unable to fetch news due to a connection error."]

import requests

def fetch_latest_news(api_key, category="general", country="us"):
    """
    Fetches the latest news headlines using the News API.

    Parameters:
        api_key (str): Your News API key.
        category (str): Category of news (e.g., general, technology, sports).
        country (str): Country code for news (e.g., us, in).

    Returns:
        list: A list of the top news headlines.
    """
    url = f"https://newsapi.org/v2/top-headlines?category={"general, technology, business, entertainment, health, science, and sports."}&country={"in"}&apiKey={"a6753501654f4010be3e58481255fb80"}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        # Debugging: Print the full API response
        print("API Response:", data)
        
        if data["status"] == "ok" and data["totalResults"] > 0:
            headlines = [article["title"] for article in data["articles"]]
            return headlines
        else:
            return ["No news found at the moment."]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return ["Unable to fetch news due to a connection error."]

# Testing the function
api_key = "your-api-key"  # Replace with your actual NewsAPI key
headlines = fetch_latest_news(api_key)
print("Headlines:", headlines)

