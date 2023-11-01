# pcost.py

file_name = "Data/portfolio.dat"


def portfolio_cost(file_name: str) -> float:
    sum = 0.0
    with open(file_name) as file:
        for line in file:
            _, shares, price = line.split()
            try:
                sum += float(shares) * float(price)
            except ValueError as e:
                print(f"Couldn't parse:", repr(line))
    return sum


if __name__ == "__main__":
    print(portfolio_cost(file_name))
