# importing the necessary dependencies
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
import os
import pandas as pd
from dependencies import textToCsv, predictionBody

# creating a router
router = APIRouter()

# creating an endpoint
@router.post("/sentimentAnalysis", tags=["Prediction"])
async def sentimentAnalysis(file: UploadFile = File(...)):

   # saving the file
   filePath = os.path.join(os.getcwd(), "uploaded_files", file.filename)
   with open(filePath, "wb") as f:
       f.write(await file.read())
   
   # reading the file
   with open(filePath, 'r') as file:
       data = file.read()

   # converting the text file into processable csv file
   processedData = textToCsv.parseTextToCSV(data)

   # reading the csv file into data frame
   dataFrameData = pd.read_csv(processedData)

   # doing prediction and fomring the json body
   result = predictionBody.formBody(dataFrameData)
   
   return JSONResponse(content=result, status_code=200)
