import csv

input_file = "conn.log"
output_file = "model/conn.csv"
fields = []

with open(input_file, "r") as infile, open(output_file, "w", newline='') as outfile:
    writer = None
    for line in infile:
        if line.startswith('#fields'):
            fields = line.strip().split('\t')[1:]
            writer = csv.DictWriter(outfile, fieldnames=fields)
            writer.writeheader()
        elif line.startswith('#'):
            continue
        else:
            if writer is None:
                continue
            values = line.strip().split('\t')
            if len(values) == len(fields):
                writer.writerow(dict(zip(fields, values)))
