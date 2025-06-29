from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def Home(query: str = ""):
    return {"message": "Hello, World!", "query": query}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
