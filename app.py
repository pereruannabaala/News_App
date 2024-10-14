# import libraries
from flask import Flask, render_template, request
from newsapi import NewsApiClient

# init flask app
app = Flask(__name__)

#init news api
newsapi = NewsApiClient(api_key='2f9f6b1d5dc84e59b18f0cf8d999d3be')