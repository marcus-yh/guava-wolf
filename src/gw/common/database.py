from pymongo import MongoClient

USER_NAME = "root"
PASSWORD = "Linux4Ever"
IP_ADDRESS_DB = "10.10.0.104"

__client = None
__db = None
__collection = None

def connect():
    """Setup database client."""
    global __client
    __client = MongoClient(f"mongodb://{USER_NAME}:{PASSWORD}@{IP_ADDRESS_DB}")


def use(name):
    """Select a database."""
    global __db
    __db = __client[name]


def collection(name):
    """Select a collection"""
    global __collection
    __collection = __db[name]


def add_record(data):
    """Add a database record."""
    return __db.metrics_collection.insert_one(data)


def find_records(query={}, projection={}):
    """Get records from database."""
    return __collection.find(query, projection)