#FastAPI with body and multiple methods within 1 fastAPI
#Includes Azure SQL DB connection (insert and select)
from typing import Optional
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseSettings

import pyodbc
import collections
import json

def insert_row(conn,insert_sql):
    cursor = conn.cursor()
    cursor.execute(insert_sql)
    print("Record inserted succesfully")
    conn.commit()

def select_rows(conn,sql_stmt):
    with conn.cursor() as cursor:
        cursor.execute(sql_stmt)
        rows = cursor.fetchall()
    objects_list = []
    if len(rows) > 0:
        for row in rows:
            d = collections.OrderedDict()
            d["id"] = row[0]
            d["crust"] = row[1]
            d["topping"] = row[2]
            objects_list.append(d)
    j = json.dumps(objects_list)
    return j

def connect_db():
    connectionstr = 'DRIVER=' + order_info.driver + ';Server=tcp:' + order_info.servername + '.database.windows.net,1433;Database=' + order_info.database + ';Uid=' + order_info.userid + ';Pwd=' + order_info.password + ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'
    conn = pyodbc.connect(connectionstr)
    print("Connection sucessful")
    return conn

class Order_info(BaseSettings):
    #app_name: str = "Awesome API"
    order_id: int = 0
    servername = 'xxxxxxxxxxxx'
    database = 'xxxxxxxx'
    userid = 'xxxxxxxxxxxxxx'
    password = 'xxxxxxxxxxx' 
    driver= '{ODBC Driver 13 for SQL Server}'

#uvicorn fastAPI1:app --reload
class orders(BaseModel):
    id: Optional[str] = None
    crust: str
    toppings: str
    # EXAMPLE Body
    """
    {
    "crust": "thin",
    "toppings": ["cheese","jalapenos"]
    }
    """

orders_list = []
order_info = Order_info() 
conn = connect_db()

app = FastAPI()

@app.post("/orders/")
async def create_item(order: orders):
    order_info.order_id = order_info.order_id + 1
    order_id = order_info.order_id
    order.id = order_id
    orders_list.append(order)
    insert_sql =  "INSERT INTO [dbo].[Mytable] (id, crust, toppings) VALUES ('" + str(order.id) + "','" + order.crust + "','" + order.toppings + "')"
    insert_row(conn,insert_sql)
    return orders_list

@app.get("/orders/")
async def get_all_orders():
    sql_stmt = "SELECT * FROM [dbo].[Mytable]"
    orders_str = select_rows(conn,sql_stmt)
    orders_json = json.loads(orders_str)
    return orders_json
    #return {"Order List" : orders_list}

@app.get("/orders/{option}")
async def get_orders(option : int):
    sql_stmt = "SELECT * FROM [dbo].[Mytable] WHERE id = " + str(option)
    orders_str = select_rows(conn,sql_stmt)
    orders_json = json.loads(orders_str)
    #print(orders_json)
    return orders_json

#@app.post()
#@app.put()
#@app.delete()

#@app.get("/items/{item_id}")
#async def read_item(item_id : int):
#    return {"item_id": item_id}

#@app.get("/items/")        http://127.0.0.1:8000/items/?skip=0&limit=10
#async def read_item(skip: int = 0, limit: int = 10):
#    return fake_items_db[skip : skip + limit]
