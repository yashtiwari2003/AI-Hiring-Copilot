from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Hiring Copilot API is running"}
