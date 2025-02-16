from flask import Flask as fk,render_template as rd,redirect as re,url_for
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.request as ur
from dotenv import load_dotenv as dot
import gridfs as gr
import os
import base64 as bs
from flask import request
url='mongodb+srv://govind_project0:interferenceowl@cluster0.zes1k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(url, server_api=ServerApi('1'))
mydb = client["GOVIND"]
mycol = mydb["GeoSync"]
fs=gr.GridFS(mydb)


app=fk(__name__,template_folder="templates")

@app.route('/',methods=['POST','GET'])
def start_page():
    return rd('main_page.html')


@app.route('/details',methods=['POST','GET'])
def detail_page():
    return "Work in Progress"


@app.route('/results',methods=['POST','GET'])
def result_page():
    return rd('result_page.html')


@app.route('/about',methods=['POST','GET'])
def about_page():
    return "Work in Progress"

@app.route('/admin')
def admin_page():
    return rd('admin_page.html')

@app.route('/admin', methods=['POST'])
def admin_page_data_send():
    id_data = request.form.get('id')
    des_data = request.form.get('des')
    date_data=request.form.get('date')
    time_data=request.form.get('time')

    # Handle file upload
    if 'img' not in request.files:
        return "No image part in the request", 400
    data_img = request.files['img']

    if data_img.filename == '':
        return "No file selected for upload", 400

    # Save file in MongoDB or process it as needed
    try:
        image_id = fs.put(data_img, filename=data_img.filename)

        # Insert data into the database
        insert_data = {
            "id": id_data,
            "date":date_data,
            "des": des_data,
            "time":time_data,
            "image_id": str(image_id)
        }
        final_data = mycol.insert_one(insert_data)
        return f"Data inserted successfully with ID: {final_data.inserted_id}", 200
    except Exception as e:
        return f"An error occurred: {e}", 500

