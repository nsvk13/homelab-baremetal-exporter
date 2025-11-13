import psutil  # type: ignore
from prometheus_client import Gauge

cpu_usage_total = Gauge("cpu_usage_percent_total", "Total CPU usage")
cpu_per_core = Gauge("cpu_usage_percent_core", "CPU usage per core", ["core"])
cpu_temp = Gauge("cpu_temperature_celsius", "CPU temperature")


def get_temp():
    if hasattr(psutil, "sensors_temperatures"):
        temps = psutil.sensors_temperatures()  # type: ignore[attr-defined]
        if "k10temp" in temps:
            return temps["k10temp"][0].current
        if "coretemp" in temps:
            return temps["coretemp"][0].current
    return None


def collect_cpu():
    cpu_usage_total.set(psutil.cpu_percent())

    for i, p in enumerate(psutil.cpu_percent(percpu=True)):
        cpu_per_core.labels(core=str(i)).set(p)

    t = get_temp()
    if t:
        cpu_temp.set(t)