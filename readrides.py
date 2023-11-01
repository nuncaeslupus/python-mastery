# readrides.py

import csv
from collections import namedtuple
from typing import Any


class Row:
    def __init__(self, route, date, daytype, rides) -> None:
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


RowTuple = namedtuple("RowTuple", ["route", "date", "daytype", "rides"])


class RowSlots:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route, date, daytype, rides) -> None:
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_tuples(filename) -> list[Any]:
    """
    Read the bus ride data as a list of tuples
    """
    print("tuples")
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dicts(filename) -> list[dict[str, Any]]:
    """
    Read the bus ride data as a list of dictionaries
    """
    print("dictionaries")
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = {
                "route": row[0],
                "date": row[1],
                "daytype": row[2],
                "rides": int(row[3]),
            }
            records.append(record)
    return records


def read_rides_as_classes(filename) -> list[Row]:
    """
    Read the bus ride data as a list of Row
    """
    print("classes")
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = Row(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


def read_rides_as_namedtuples(filename) -> list[RowTuple]:
    """
    Read the bus ride data as a list of RowTuple
    """
    print("namedtuples:")
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = RowTuple(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


def read_rides_as_slots(filename) -> list[RowTuple]:
    """
    Read the bus ride data as a list of RowSlots
    """
    print("slots:")
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = RowSlots(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    # slots < tuples < namedtuples << classes << dictionaries
    # rows = read_rides_as_tuples("Data/ctabus.csv")
    # rows = read_rides_as_dictionaries("Data/ctabus.csv")
    # rows = read_rides_as_classes("Data/ctabus.csv")
    # rows = read_rides_as_namedtuples("Data/ctabus.csv")
    rows = read_rides_as_slots("Data/ctabus.csv")
    print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
