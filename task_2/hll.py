import json
import time
from datasketch import HyperLogLog

file_name = "task_2/lms-stage-access.log"
hll = HyperLogLog(p=14)
ip_list = []

with open(file_name, "r") as f:
    for line in f:
        try:
            data = json.loads(line)
            ip = data.get("remote_addr")
            if ip:
                ip_list.append(ip)
        except json.JSONDecodeError:
            continue

start = time.time()
ip_set = set(ip_list)
time_exact = time.time() - start

start = time.time()
for ip in ip_list:
    hll.update(ip.encode("utf-8"))
unique_hll = hll.count()
time_hll = time.time() - start

print("Результати порівняння:")
print(f"{'':<25}{'Точний підрахунок':>20}{'HyperLogLog':>15}")
print(f"{'Унікальні елементи':<25}{len(ip_set):>20}{unique_hll:>15}")
print(f"{'Час виконання (сек.)':<25}{time_exact:>20.4f}{time_hll:>15.4f}")
