import psutil

disk_path = "/"
cpu_interval = 1

def cpu_usage(interval: int = 0):
    return psutil.cpu_percent(interval=interval)

def disk_usage(path: str = "/"):
    return psutil.disk_usage(path).percent

def mem_usage():
    return psutil.virtual_memory().percent

def bytes_received():
    return psutil.net_io_counters().bytes_recv

def bytes_sent():
    return psutil.net_io_counters().bytes_sent

def get_metrics():
    return {'cpu': cpu_usage(cpu_interval),
            'disk': disk_usage(disk_path),
            'mem': mem_usage(),
            'bytes_recv': bytes_received(),
            'bytes_sent': bytes_sent()}
