#!/usr/bin/env python3

import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def links():
    i = 0
    first = 320
    baseUrl = "https://content.developernation.net/"
    returnVal = 200
    url = []
    #     while returnVal != 404 and i <= 6:
    while returnVal != 404:
        response = requests.head(baseUrl + str(first + i))
        url.append(baseUrl + str(first + i))
        returnVal = response.status_code
        i = i+1
    
    #return the list of URl - the last one since last one is not yet live
    return render_template("index.html", url=url[:-1])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)


    



