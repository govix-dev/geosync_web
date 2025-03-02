from dotenv import load_dotenv
import os
load_dotenv()
import cloudinary 
import cloudinary.uploader
import cloudinary.api

cloudinary.config(

cloud_name=os.getenv("cloud_name"),
api_key=os.getenv("api_key"),
api_secret=os.getenv("api_secret")
)