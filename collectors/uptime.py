from prometheus_client import Gauge
import psutil
import time

uptime = Gauge("system_uptime_seconds", "System uptime in seconds")

def collect_uptime():
    uptime.set(time.time() - psutil.boot_time())