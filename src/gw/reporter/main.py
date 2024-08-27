import socket
from datetime import datetime
from gw.common import database
from gw.reporter import metrics


def main():
    database.connect()
    database.select("metric_db")
    data = {
        'timestamp': datetime.now(),
        'hostname': socket.gethostname(),
        'metrics': metrics.get_metrics()
    }
    database.add_record(data)


if __name__ == "__main__":
    main()

