import re
from datetime import datetime as dt

date_pattern = re.compile(r"^\d{2}/\d{2}/\d{4}$")


def read_valid_dates(file_path: str) -> list[str]:
    try:
        f = open(file_path, "r")
    except FileNotFoundError:
        raise FileNotFoundError(f"Specified path: '{file_path}' doesn't exists")

    dates = []
    for i, line in enumerate(f):
        line = line.strip()

        if date_pattern.fullmatch(line) is None:
            print(error(i, line, "it doesn't match de pattern dd/mm/yyyy"))
            continue

        try:
            date = dt.strptime(line, "%d/%m/%Y")
            dates.append(date)
        except ValueError as e:
            print(error(i, line, e))

    dates.sort()
    return [d.date().isoformat() for d in dates]


def error(index, line, reason) -> str:
    return f"WARNING | Malformed line #{index} @ ({line}) due {reason}"