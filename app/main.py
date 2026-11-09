from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Items API", version="1.0.0")


class ItemIn(BaseModel):
    name: str
    description: str | None = None


class Item(ItemIn):
    id: int


items: dict[int, Item] = {}
next_id = 1


@app.get("/api/items", response_model=list[Item])
def list_items():
    return list(items.values())


@app.get("/api/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.post("/api/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(data: ItemIn):
    global next_id
    item = Item(id=next_id, **data.model_dump())
    items[next_id] = item
    next_id += 1
    return item


@app.put("/api/items/{item_id}", response_model=Item)
def update_item(item_id: int, data: ItemIn):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = Item(id=item_id, **data.model_dump())
    return items[item_id]


@app.delete("/api/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)