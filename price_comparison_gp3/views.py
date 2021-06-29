from django.http import HttpResponse
import requests


def index(request):
    url = "https://amazon-products1.p.rapidapi.com/product"

    querystring = {"country":"US","asin":"B08BF4CZSV"}

    headers = {
        'x-rapidapi-key': "dfde2332c1msh5e02a5213a8e314p11a43cjsn838ef6cd0689",
        'x-rapidapi-host': "amazon-products1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return HttpResponse(response)

def index2(request):
    url = "https://ebay-products.p.rapidapi.com/product"

    querystring = {"url":"https%3A%2F%2Fwww.ebay.co.uk%2Fitm%2FBox-Celeron-15-6-Quad-Core-Laptop-4GB-Ram-500GB-Wireless%2F274237631139"}

    headers = {
        'x-rapidapi-key': "dfde2332c1msh5e02a5213a8e314p11a43cjsn838ef6cd0689",
        'x-rapidapi-host': "ebay-products.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)