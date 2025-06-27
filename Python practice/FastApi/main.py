from fastapi import FastAPI
import uvicorn
app = FastAPI()

# @app.get("/")
# async def Home():
#     return {
#         "id": 1,
#         "status": 200,
#         "title": "Ipad M-10",
#         "price": 100000,
#         "description": "Ipad M-10 is a great product"
#     }

# @app.get("/")
# async def Home():
#     return {
#         "product": {
#             "id": 1,
#             "status": 200,
#             "title": "Ipad M-10",
#             "price": 100000,
#             "description": "Ipad M-10 is a great product"
#         }
#     }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
