# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import csv
import json
def read_from_file():
    with open('csv_file.txt') as f:
        return list(csv.DictReader(f, fieldnames=['club', 'city', 'country']))


with open('json_file.txt', 'w') as f:
    json.dump(read_from_file(), f)
