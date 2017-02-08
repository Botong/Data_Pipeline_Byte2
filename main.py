# Imports
import os
import jinja2
import webapp2
import logging
import json
import urllib

# this is used for constructing URLs to google's APIS
from googleapiclient.discovery import build

API_KEY = 'AIzaSyADiwBc0are9WMVyRRiPDz1ZIuZPA0OkyY'
TABLE_ID = '1O3JunhDFtViea0ubyBRqkpgbcbn0O13WHffgEsSO'

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
# This uses discovery to create an object that can talk to the 
# fusion tables API using the developer key
#service = build('fusiontables', 'v1', developerKey=API_KEY)
#request = service.column().list(tableId=TABLE_ID)
#query = "SELECT * FROM " + TABLE_ID + " WHERE  Status = 'Accepted' LIMIT 50"
#response = service.query().sql(sql=query).execute()
#cols = response['columns']
#logging.info(cols)
#rows = response['rows']
#logging.info(response['rows'])
    
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    return template.render()

@app.route('/table')
def table():
    template = JINJA_ENVIRONMENT.get_template('templates/table.html')
    return template.render()

#def get_all_data(self):
#    query = "SELECT * FROM " + TABLE_ID + " WHERE  AnimalType = 'DOG' LIMIT 2"
#    response = service.query().sql(sql=query).execute()
#    cols = response['columns']
#    logging.info(cols)
#    rows = response['rows']
#    logging.info(response['rows'])
#    return template.render(headers=cols, content=rows)

@app.route('/quality')
def quality():
	template = JINJA_ENVIRONMENT.get_template('templates/quality.html')
	return template.render()

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
