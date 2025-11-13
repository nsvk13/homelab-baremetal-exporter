from prometheus_client import Gauge
import psutil

ram_used = Gauge("ram_used_gb", "RAM used in GB")
ram_free = Gauge("ram_free_gb", "RAM free in GB")


def collect_memory():
    mem = psutil.virtual_memory()
    ram_used.set((mem.total - mem.available) / (1024**3))
    ram_free.set(mem.available / (1024**3))