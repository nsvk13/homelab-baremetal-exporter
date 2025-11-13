from prometheus_client import Gauge
import psutil

disk_usage = Gauge("disk_usage_percent", "Disk usage in percent", ["device"])

def collect_disks():
    for p in psutil.disk_partitions():
        try:
            u = psutil.disk_usage(p.mountpoint)
            disk_usage.labels(deice=p.mountpoint).set(u.percent)
        except PermissionError:
            pass