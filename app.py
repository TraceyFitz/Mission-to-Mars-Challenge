#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The first line says that we'll use Flask to render a template, redirecting to another url, and creating a URL.
# The second line says we'll use PyMongo to interact with our Mongo database.
# The third line says that to use the scraping code, we will convert from Jupyter notebook to Python.
# Under these lines, let's add the following to set up Flask:

from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping


# tell Python how to connect to Mongo using PyMongo
# app.config["MONGO_URI"] tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL.
# "mongodb://localhost:27017/mars_app" is the URI we'll be using to connect our app to Mongo. This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named "mars_app".
app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://localhost:27017/mars_app'
mongo = PyMongo(app)


# In[2]:


#10.5.1 Set up/define  App/Flask Routes. Flask routes bind URLs to functions
#one for the main HTML page everyone will view when visiting the web app, 
#and one to actually scrape new data using the code we've written
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)
# This route, @app.route("/"), tells Flask what to display when we're looking at the home page, index.html (index.html is the default HTML file that we'll use to display the content we've scraped). This means that when we visit our web app's HTML page, we will see the home page.
# Within the def index(): function the following is accomplished:
# mars = mongo.db.mars.find_one() uses PyMongo to find the "mars" collection in our database, which we will create when we convert our Jupyter scraping code to Python Script. We will also assign that path to themars variable for use later.
# return render_template("index.html" tells Flask to return an HTML template using an index.html file. We'll create this file after we build the Flask routes.
# , mars=mars) tells Python to use the "mars" collection in MongoDB.
# This function is what links our visual representation of our work, our web app, to the code that powers it.


# In[ ]:


# Our next function will set up our scraping route. Bottom of 10.5.1 for explanation
# This route will be the "button" of the web application, 
# the one that will scrape updated data when we tell it to from the homepage of our web app. 
# It'll be tied to a button that will run the code when it's clicked.
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    data = scraping.scrape_all()
    mars.update_one({}, data, upsert=True)
    return redirect('/', code=302)
if __name__ == "__main__":
   app.run(debug=True)


# In[ ]:




