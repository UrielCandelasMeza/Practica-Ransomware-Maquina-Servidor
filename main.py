from fastapi import FastAPI
from src.models.ransomware import Ransomware

app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.post("/ransomware")
async def ransomware(keys: Ransomware):
  print(keys)
  return keys