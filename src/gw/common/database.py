from pymongo import MongoClient

USER_NAME = "root"
PASSWORD = "Linux4Ever"
IP_ADDRESS_DB = "10.10.0.104"
DATABASE = "metrics_db"

__client = None
__db = None

def connect():
    """Setup database client."""
    global __client
    __client = MongoClient(f"mongodb://{USER_NAME}:{PASSWORD}@{IP_ADDRESS_DB}")

def select(name):
    """Select a database."""
    global __db
    __db = __client[name]

def add_record(data):
    """Add a database record."""
    __db.metrics_collection.insert_one(data)

def get_records(start_date, end_date):
    """Get records between dates."""
    pass