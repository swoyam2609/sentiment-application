from fastapi import APIRouter, File, UploadFile
import os

router = APIRouter()

@router.post("/sentimentAnalysis", tags=["Prediction"])
async def sentimentAnalysis(file: UploadFile = File(...)):
    file_path = os.path.join(os.getcwd(), "uploaded_files", file.filename)
    with open(file_path, "wb") as f:
       f.write(await file.read())
    return {"message": "Files uploaded successfully"}