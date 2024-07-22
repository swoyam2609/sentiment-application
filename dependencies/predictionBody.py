import pandas as pd
from dependencies import textClassification

def formBody(input: pd.DataFrame):
    body = []
    predictions = {'positive': 0, 'neutral': 0, 'negative': 0}
    count = 0

    for index, row in input.iterrows():
        temp = {}
        if row['Agent/Customer'] == 'Customer':
            temp['userType'] = 1
            temp['message'] = row['Message']
            prediction = textClassification.predict(row['Message'])  # Adjust as necessary
            temp['prediction'] = prediction
            for i in prediction[0]:
                if(i['label']=='positive'):
                    predictions['positive'] += i['score']
                elif(i['label']=='neutral'):
                    predictions['neutral'] += i['score']
                elif(i['label']=='negative'):
                    predictions['negative'] += i['score']
            count += 1
        else:
            temp['userType'] = 0
            temp['message'] = row['Message']
        
        body.append(temp)
    predictions['positive'] /=count
    predictions['neutral'] /=count
    predictions['negative'] /=count

    responseBody = {
        "overallResult":predictions,
        "individualResult":body

    }
    return responseBody

