from fastapi import FastAPI
from pydantic import BaseModel
app =FastAPI()
class User(BaseModel):
    name: str
@app.get("/")
def home():
    return{"message": "/fastapi backend is running!"}
@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI!"}
@app.post("/greet")
def greet_user(user: User):
    return {"message": f"Hello {user.name}!"}