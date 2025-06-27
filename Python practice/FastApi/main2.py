from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn
import enum

app = FastAPI()

class Role(enum.Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


@app.get("/user")
async def user(role: Role):
    if role == Role.ADMIN:
        return JSONResponse(content={
            "status": "success",
            "data": role.value
        }, status_code=status.HTTP_200_OK)
    elif role == Role.USER:
        return JSONResponse(content={
            "status": "success",
            "data": role.value
        }, status_code=status.HTTP_200_OK)
    elif role == Role.GUEST:
        return JSONResponse(content={
            "status": "success",
            "data": role.value
        }, status_code=status.HTTP_200_OK)      
    else:
        return JSONResponse(content={
            "status": "success",
            "data": role.value
        }, status_code=status.HTTP_200_OK)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)