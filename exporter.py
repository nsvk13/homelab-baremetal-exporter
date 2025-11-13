from prometheus_client import start_http_server
from collectors.cpu import collect_cpu

import time

if __name__ == "__main__":
    start_http_server(9101)

    while True:
        collect_cpu()
        time.sleep(2)