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

# this function will return sources and domains in str format
# each of them separated by a comma
def get_source_and domains():
    all_sources = newsapi.get_sources()['sources']
    sources = []
    domains = []
    for e in all_sources:
        id = e['id']
        domain = e['url'].replace("https://", "")
        domain = domain.replace("https://","")
        domain = domain.replace("www.","")
        slash = domain.find('/')
        if slash != -1:
            domain = domain[:slash]
        sources.append(id)
        domains.append(domain)
    sources = ",".join(sources)
    domains = ",".join(domains)
    return sources,domains

# in post request
sources, domains = get_sources_and_domains()
related_news = newsapi.get_everything(q=keyword,
                                      sources=sources,
                                      domains=domains,
                                      language='en',
                                      sort_by='relevancy')



                                      