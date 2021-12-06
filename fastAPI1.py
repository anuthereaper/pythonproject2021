from fastapi import FastAPI

#uvicorn fastAPI1:app --reload
#http://127.0.0.1:8000/docs
# https://fastapi.tiangolo.com/tutorial/body/

app = FastAPI()

@app.get("/booze")
async def root():
    print("hello,world")
    return {"Booze":["Whiskey","Vokda","Beer"]}

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
