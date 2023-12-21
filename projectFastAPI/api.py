from fastapi import FastAPI

app = FastAPI()

database = {}

@app.get("/get_data/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "data": database.get(item_id, "Not found")}


@app.post("/add_data/{item_id}")
def add_item(item_id: int, data: str):
    database[item_id] = data
    return {"item_id": item_id, "data": data}


#! uvicorn api:app --reload