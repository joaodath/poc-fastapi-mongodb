from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}

# add basic structure to api


@app.post("/graph") #save graph
def post_graph(graph: dict):
    return {"graph": graph}


@app.get("/graph/{graph_id}") #recover graph
def get_graph(graph_id: int):
    return {"graph_id": graph_id}

# todo: request clarification about the last two endpoints