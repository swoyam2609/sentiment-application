from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
import os
import pandas as pd
from dependencies import textToCsv, predictionBody

router = APIRouter()


@router.post("/sentimentAnalysis", tags=["Prediction"])
async def sentimentAnalysis(file: UploadFile = File(...)):
   filePath = os.path.join(os.getcwd(), "uploaded_files", file.filename)
   with open(filePath, "wb") as f:
       f.write(await file.read())
   
   with open(filePath, 'r') as file:
       data = file.read()

   processedData = textToCsv.parseTextToCSV(data)
   dataFrameData = pd.read_csv(processedData)
   result = predictionBody.formBody(dataFrameData)
   return JSONResponse(content=result, status_code=200)
