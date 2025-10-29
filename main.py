from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return FileResponse("static/index.html", media_type="text/html; charset=utf-8")

@app.get("/download-cv")
def download_cv():
    headers = {"Content-Disposition": "attachment; filename=\"CV.pdf\""}
    return FileResponse("static/files/CV.pdf", media_type="application/pdf", headers=headers)

    
