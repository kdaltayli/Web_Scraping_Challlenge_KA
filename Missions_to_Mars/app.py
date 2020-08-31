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

    #find one record of data from the mono database
    destination_data=mongo.db.collection.find_one()

    #Return template and data
    return render_template("index.html", list=destination_data)

#Route that will trigger the scrape funtion
@app.route("/scrape")
def scrape():

    #Run the scrape function
    mars_mission=scrape_mars.scrape_info()
    # mars_image=scrape_mars.space_image()
    # mars_fact=scrape_mars.mars_fact()
    # space_imag=scrape_mars.space_image()

    # dict={"mars_mission_title":news[0],"mars_mission_parag":paragraph[1],
    #      "mars_image_url":image_url,"mars_fact_table":result_table,"space_image_url":hemisphere_image_url}
    dict={"mars_mission_title":news[0],"mars_mission_parag":paragraph[1]}
    mongo.db.collection.update({},dict,upsert=True)
    return redirect("/") 

if __name__=="__main__":
    app.run(debug=True)