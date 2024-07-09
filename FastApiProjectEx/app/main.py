from typing import Any

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# path parameter 를 사용한 GET API.
@app.get("/path-items/{item_id}")
async def read_item_by_path(item_id: int) -> dict[str, Any]:
    return {"item_id": item_id}

# query parameter 를 사용한 GET API.
@app.get("/query-items")
async def read_item_by_query(item_id: int) -> dict[str, Any]:
    return {"item_id": item_id}


class Item(BaseModel):
    id: int
    name: str

# BaseModel 을 사용한 POST API.
@app.post("/model-items")
async def create_item_by_model(item: Item) -> Item:
    return item

# body 를 사용한 POST API.
@app.post("/body-items")
async def create_item_by_body(
    id: int = Body(embed=True), name: str = Body(embed=True)
) -> dict[str, Any]:
    item = {"id": id, "name": name}
    return item