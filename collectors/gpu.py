from prometheus_client import Gauge
import subprocess

gpu_temp = Gauge("gpu_temperature_celsius", "GPU temperature")

def collect_gpu():
    try:
        out = subprocess.check_output(["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader"], stderr=subprocess.DEVNULL)
        t = int(out.decode().strip())
        gpu_temp.set(t)
    except:
        pass