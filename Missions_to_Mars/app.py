from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars

#create instance of Flask App
app=Flask(__name__)

#Use PyMongo to establish Mongo connection
# app.config['MONGO_URI']="mongodb://localhost:27017//mission_mars"
# mongo=PyMongo(app)
mongo=PyMongo(app, uri="mongodb://localhost:27017/mission_mars")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    destination_data=mongo.db.mars_data.find_one()

    #Return template and data
    return render_template("index.html", list=destination_data)

#Route that will trigger the scrape funtion
@app.route("/scrape")
def scrape():

    destination_data=mongo.db.mars_data

    #Run the scrape function
    mars_mission=scrape_mars.scrape_info()
   
   #insert the mars mission data in to the collection
    destination_data.update({},mars_mission,upsert=True)

    # Go back to home page
    return redirect("/") 

if __name__=="__main__":
    app.run(debug=True)