from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGO_URI")
DB_NAME = "assessment_db"

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]

async def init_indexes():
    await db.employees.create_index("employee_id", unique=True)
    
async def init_schema():
    employee_schema = {
        "validator": {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["employee_id", "name", "department", "salary", "joining_date", "skills"],
                "properties": {
                    "employee_id": {"bsonType": "string"},
                    "name": {"bsonType": "string"},
                    "department": {"bsonType": "string"},
                    "salary": {"bsonType": "double"},
                    "joining_date": {"bsonType": "date"},
                    "skills": {"bsonType": "array", "items": {"bsonType": "string"}}
                }
            }
        }
    }
    try:
        await db.create_collection("employees", **employee_schema)
    except Exception:
        pass

def get_db():
    return db