from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Funciona!"}

@app.get("/ping")
def ping():
    return {"status": True}
