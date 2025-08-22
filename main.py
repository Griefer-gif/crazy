from fastapi import FastAPI

app = FastAPI()

@app.get("/dadadada")
async def read_root():
    return {"message": "Hello World"}

@app.get("/testdadadae1")
async def funcaoteste():
    return {"message": "teste ologoo"}