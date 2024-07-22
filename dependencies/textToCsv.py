# importing the necessay dependencies
import csv
import re
import random

# function to convert from txt file to required csv file
def parseTextToCSV(input: str):
    lines = input.strip().split('\n')
    iterator = iter(lines)
    data = []

    # iterating through conversation and matching regex
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
    csvFile = f'uploaded_files/conversation{random.randint(0,100)}.csv'
    with open(csvFile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Agent/Customer', 'Time', 'Message'])
        writer.writerows(data)

    return csvFile