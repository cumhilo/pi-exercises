from datetime import datetime as dt

# TODO: improve the code
def read_valid_dates(file_path: str) -> list[str]:
    try:
        f = open(file_path, "r")
    except FileNotFoundError:
        raise FileNotFoundError(file_path)

    dates = []
    for line in f:
        line = line.strip()
        split = line.split("/")

        # EXTRA NOT NEEDED CHECKS
        if len(split) != 3 or len(line) != len("dd/mm/yyyy"):
            continue

        try:
            day = int(split[0])
            month = int(split[1])
            year = int(split[2])

            if day < 1 or month < 1 or year < 1:
                continue

            if day > 31 or month > 12:
                continue
        except ValueError:
            continue

        try:
            date = dt.strptime(line, "%d/%m/%Y")
            dates.append(date)
        except ValueError:
            continue

    dates.sort()
    return [d.date().isoformat() for d in dates]