from fastapi import FastAPI, Query
from .password_generator import generate_password

app = FastAPI(title="Password Generator")

@app.get("/generate")
def generate(length: int = Query(12, ge=4, le=128),
             use_upper: bool = True,
             use_lower: bool = True,
             use_digits: bool = True,
             use_symbols: bool = False):
    pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    return {"password": pwd}

@app.get("/")
def read_root():
    return {"message": "Password Generator API is running. Go to /docs for interactive UI."}
