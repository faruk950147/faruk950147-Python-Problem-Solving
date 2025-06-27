from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn
app = FastAPI()

@app.get("/")
async def Home():
    return JSONResponse(content={
        "status": "success",
        "data": "Hello World"
    }, status_code=status.HTTP_200_OK)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)