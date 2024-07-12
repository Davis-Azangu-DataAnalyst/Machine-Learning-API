from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def status_check():
    return {"status": "API is Online..."}



