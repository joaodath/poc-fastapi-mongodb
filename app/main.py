import os
from typing import List, Optional
from fastapi import FastAPI

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(raise_error_if_not_found=True))

from .database.database import find_all
from .database.models import Graph, GraphList

app = FastAPI()

@app.get("/", description="A route to get all graphs stored", response_model=List[GraphList])
async def find_all():
    graphs = await find_all(GraphList)
    return graphs
# add basic structure to api

@app.get("/graph/{graph_id}")  # recover graph
def get_graph(graph_id: int):

    return {"graph_id": graph_id}

# todo: request clarification about the last two endpoints
