#fastAPI with body and multiple methods within 1 fastAPI
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

#uvicorn fastAPI1:app --reload
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    # EXAMPLE Body
    """
    {
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
    }
    """

item_list = []
test_item = {
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
    }
item_list.append(test_item)    
app = FastAPI()

#@app.get("/items/{item_id}")
#async def read_item(item_id : int):
#    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    item_list.append(item)
    return item

@app.get("/items/{option}")
async def get_items(option : str):
    if option == 'list':
        return item_list
#app.include_router(router)
#if __name__ == "__main__":
#    app.run(debug=True)


#@app.post()
#@app.put()
#@app.delete()

#@app.get("/items/{item_id}")
#async def read_item(item_id : int):
#    return {"item_id": item_id}

#@app.get("/items/")        http://127.0.0.1:8000/items/?skip=0&limit=10
#async def read_item(skip: int = 0, limit: int = 10):
#    return fake_items_db[skip : skip + limit]
