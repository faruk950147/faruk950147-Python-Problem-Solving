from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn
app = FastAPI()

# @app.get("/")
# def Home():
#     return {
#         "Status": 200,
#         "data": "Hello World"
#     }

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

@app.get("/")
def Home():
    return JSONResponse(content={"data": "Hello World"}, status_code=status.HTTP_200_OK)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return JSONResponse(content={"item_id": item_id, "q": q}, status_code=status.HTTP_200_OK)

@app.post("/items")
def create_item(item_id: int, q: str = None):
    return JSONResponse(content={"item_id": item_id, "q": q}, status_code=status.HTTP_201_CREATED)

@app.put("/items/{item_id}")
def update_item(item_id: int, q: str = None):
    return JSONResponse(content={"item_id": item_id, "q": q}, status_code=status.HTTP_200_OK)

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return JSONResponse(content={"item_id": item_id}, status_code=status.HTTP_200_OK)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
