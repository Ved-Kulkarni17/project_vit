import csv

input_file = "conn.log"
output_file = "conn.csv"
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
                row = dict(zip(fields, values))
                # Convert label if present
                if 'label' in row:
                    if row['label'] == 'Background':
                        row['label'] = 0
                    elif row['label'] == 'Benign':
                        row['label'] = 0
                    elif row['label'] == 'Malicious':
                        row['label'] = 1
                    row['label'] = int(row['label'])
                writer.writerow(row)
    


