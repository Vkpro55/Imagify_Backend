import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the .env file

# Retrieve the connection URL from the environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Check if the DATABASE_URL is being read correctly
if not DATABASE_URL:
    raise ValueError("No DATABASE_URL found in environment variables")

# Create the MongoDB client
client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)

# Get the 'test' database (it will default to 'test' if not specified in the URL)
db = client.get_database()  # This will automatically use the 'test' database
