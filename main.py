from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {
        'message' : 'Hellow World (^_^)' 
    }

@app.get("/about")
def about():
    return {
        'message' : 'I have started learning FastAPI'
    }