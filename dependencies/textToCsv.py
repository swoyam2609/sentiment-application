import csv
import re

def parseTextToCSV(input: str):
    lines = input.strip().split('\n')
    iterator = iter(lines)
    data = []

    for line in iterator:
        if line.startswith('['):
            match = re.match(r'\[(.+) (\d+:\d+)\]', line)
            if match:
                speaker = match.group(1)
                time = match.group(2)
                message = next(iterator).strip()
                data.append([speaker, time, message])
        else:
            data[-1][-1] += ' ' + line.strip()

    # Writing to a CSV file
    csv_file = 'conversation.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Agent/Customer', 'Time', 'Message'])
        writer.writerows(data)

    return csv_file