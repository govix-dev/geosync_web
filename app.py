from flask import Flask as fk,render_template as rd,redirect as re,url_for,jsonify

import cloudinary_config
import cloudinary.uploader
from bson import ObjectId
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


    if 'img' not in request.files:
        return "No image part in the request", 400
    data_img = request.files['img']

    if data_img.filename == '':
        return "No file selected for upload", 400
    try:
        image_id = fs.put(data_img, filename=data_img.filename)

    
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

@app.route('/results', methods=['POST', 'GET'])
def result_page():
    try:
        # Fetch all documents from MongoDB
        data = list(mycol.find())

        # Get image data for each document
        for item in data:
            # Check if the item is a dictionary and if 'image_id' exists
            if isinstance(item, dict) and 'image_id' in item:
                image_id = item['image_id']
                if image_id:
                    # Correctly fetch image from GridFS using ObjectId
                    image_data = fs.get(ObjectId(image_id))
                    item['image_url'] = image_data.read()  # Add image data to each record

        # Pass the data to the result_page.html template
        return rd('result_page.html', data=data)

    except Exception as e:
        return f"An error occurred while fetching the data: {e}", 500

# Route to serve images (example)
@app.route('/image/<image_id>')
def get_image(image_id):
    try:
        image_data = fs.get(ObjectId(image_id))
        return image_data.read(), 200  # Return image data
    except Exception as e:
        return f"Image not found: {e}", 404
    
@app.route('/cloud', methods=['POST', 'GET'])
def image_cloud():
    if request.method == 'GET':
        return rd('cloud.html')  # Render the HTML page correctly

    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        try:
            upload_result = cloudinary.uploader.upload(file)
            image_url = upload_result.get('url')
            return jsonify({"url": image_url})  # Return only the URL
        except Exception as e:
            return jsonify({"error": str(e)}), 500
