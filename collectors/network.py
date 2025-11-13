from prometheus_client import Gauge
import psutil

net_up = Gauge("net_upload_bytes_sec", "Upload speed bytes/s")
net_down = Gauge("net_download_bytes_sec", "Download speed bytes/s")

_prev = psutil.net_io_counters()

def collect_network():
    global _prev

    now = psutil.net_io_counters()
    net_up.set(now.bytes_sent - _prev.bytes_sent)
    net_down.set(now.bytes_recv - _prev.bytes_recv)

    _prev = now