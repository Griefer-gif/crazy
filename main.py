from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/testeteste1")
async def funcaoteste():
    return {"message": "selooooooooooko"}