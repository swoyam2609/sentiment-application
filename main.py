from fastapi import FastAPI
import uvicorn
from  fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routers import sentimentAnalysis

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sentimentAnalysis.router)

@app.get("/", tags=["Default"])
def default():
    content = {"Backend":"working"}
    return JSONResponse(content=content, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)