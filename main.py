from typing import Union

from fastapi import FastAPI

from models import class_todo


app = FastAPI()

todo = []

@app.get("/todo")
async def read_root():
    return {"all todos": todo}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/todo")
async def insert_todo(get_todo: class_todo):
    todo.append(get_todo)
    return("one todo added", get_todo)


@app.get("todo/{item_id}")
async def show_item(item_id:int):
    for t in todo:
        if t.id == item_id:
            return{"here is the todo:": t}
    return{"Message":"could not find"}