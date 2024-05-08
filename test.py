import requests

i = 0
first = 315
baseUrl = "https://www.developernation.net/newsletter/"
returnVal = 329
url = []

while returnVal != 404:
    response = requests.head(baseUrl + str(first + i))
    url.append(baseUrl + str(first + i))
    returnVal = response.status_code
    i = i+1