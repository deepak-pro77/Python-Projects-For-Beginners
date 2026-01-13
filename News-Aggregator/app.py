import requests
from sys import argv

URL = ('https://newsapi.org/v2/top-headlines?')

API_KEY = "954d0a238882452a9d29f58edde87416"


def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)


def get_articles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)


def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []

    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')


if __name__ == "__main__":
    # print(f"Getting News for {argv[1]}...\n")
    # get_articles_by_category(argv[1])
    # print(F'Successfully retrieved top {argv[1]} headlines')
    get_articles_by_query("Liz Truss")
