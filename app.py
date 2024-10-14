# import libraries
from flask import Flask, render_template, request
from newsapi import NewsApiClient

# init flask app
app = Flask(__name__)

# init news api
newsapi = NewsApiClient(api_key='2f9f6b1d5dc84e59b18f0cf8d999d3be')

# this function rreturns a JSON object
top_headlines =newsapi.get_top_headlines(country="in", language="en")
total_results = top_headlines['totalResults']

# the maximum value for page_size parameter is 100
if total_results > 100:
    total_results = 100

# fetch articles where no. of articles=total_results
# this returns a list of articles
all_headlines = newsapi.get_top_headlines(country="in",
                                          language="en",
                                          page_size=total_results)['articles']

