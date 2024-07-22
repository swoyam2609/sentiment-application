from dependencies import textToCsv
from dependencies import textClassification
from dependencies import predictionBody

filePath = "transcripts/Udaya Good call 20th.txt"

with open(file=filePath, mode='r') as file:
    content = file.read()

data = textToCsv.parseTextToCSV(content)

import pandas as pd

dataCsv = pd.read_csv(data)

dataBody = predictionBody.formBody(dataCsv)

print(dataBody)
