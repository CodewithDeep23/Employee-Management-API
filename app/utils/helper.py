from bson import ObjectId
from datetime import datetime

def serialize_document(doc):
    if not doc:
        return None

    # Convert ObjectId
    if "_id" in doc and isinstance(doc["_id"], ObjectId):
        doc["_id"] = str(doc["_id"])

    # Convert datetime → ISO string
    for key, value in doc.items():
        if isinstance(value, datetime):
            doc[key] = value.isoformat()

    return doc