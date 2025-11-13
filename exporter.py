from prometheus_client import start_http_server
from collectors.cpu import collect_cpu
from collectors.memory import collect_memory
from collectors.disk import collect_disks
from collectors.network import collect_network
from collectors.uptime import collect_uptime
from collectors.gpu import collect_gpu

import time

if __name__ == "__main__":
    start_http_server(9101)

    while True:
        collect_cpu()
        collect_memory()
        collect_disks()
        collect_network()
        collect_uptime()
        collect_gpu()
        time.sleep(2)