# Notes

## TODO
- fixa cronjob
- fixa database.py
- fixa tester
- fixa readme
- fixa projektstruktur

## Find example - MongoDB

```python
from datetime import datetime, timedelta
from gw.common import database

database.connect()
database.use("metric_db")
database.collection("metrics_collection")

start_date = datetime.now() - timedelta(hours=24)

query = {
    "timestamp": {"$gt", start_date},
    "hostname": "host001"
}

records = database.find_records(query)
```