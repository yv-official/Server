from dotenv import load_dotenv
import os

# LoadEnvironment Varibale
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME')