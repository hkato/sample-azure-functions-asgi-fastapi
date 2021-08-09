from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str


@app.get("/hello")
async def get_hello(name: str):
    message = _hello(name)
    return {"message": message}


@app.post("/hello")
async def post_hello(item: Item):
    message = _hello(item.name)
    return {"message": message}


def _hello(name: str) -> str:
    return f"Hello, {name}. This HTTP triggered function executed successfully."


@app.get("/foo")
async def foo():
    return {"message": "test"}


@app.post("/bar")
async def bar(item: Item):
    return item
