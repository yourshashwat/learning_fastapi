from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def hello():
    return {"msg": "Hello World"}

@app.get("/about")
def about():
    return {"msg": "I will be learning everything about fastapi in this series"}