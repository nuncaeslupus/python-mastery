# datarides.py

import tracemalloc
from collections import Counter

import readrides

tracemalloc.start()

rows = readrides.read_rides_as_dicts("Data/ctabus.csv")

print(len({row["route"] for row in rows}))
print(
    [
        row["rides"]
        for row in rows
        if row["route"] == "22" and row["date"] == "02/02/2011"
    ][0]
)

c = Counter()
for row in rows:
    c[row["route"]] += row["rides"]
for route, count in c.most_common():
    print("%5s %10d" % (route, count))

ini = Counter()
end = Counter()
for row in rows:
    if "2001" in row["date"]:
        ini[row["route"]] += row["rides"]
    elif "2011" in row["date"]:
        end[row["route"]] += row["rides"]
sub = end - ini
print(sub.most_common(5))

# ---- Memory use
print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
