import uvicorn
from fastapi import FastAPI
from tinydb import TinyDB, Query

app = FastAPI()


def memory_db():
    db = TinyDB('db.json')
    return db


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# Path: bbs_api/main.py
""" Main entry point for the application """


def main():
    uvicorn.run("bbs_api.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
