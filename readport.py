# readport.py

import csv
from typing import Any


# A function that reads a file into a list of dicts
def read_portfolio(filename) -> list[Any]:
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)
        for row in rows:
            record = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(record)
    return portfolio
