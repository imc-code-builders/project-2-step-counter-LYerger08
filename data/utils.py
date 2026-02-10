import csv

def read_csv(filename):
    """Read acceleration data from a CSV file.

    Returns: times (list), magnitudes (list)
    """
    times = []
    magnitudes = []

    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            times.append(float(row['Time (seconds)']))
            magnitudes.append(float(row['strength']))

    return times, magnitudes