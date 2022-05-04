from .database.models import GraphList
from .database.database import find_all, find_one_by_id
from typing import List
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(raise_error_if_not_found=True))


app = FastAPI()


@app.get("/allgraphs", description="A route to get all graphs stored", response_model=List[GraphList])
async def get_all():
    graphs = await find_all(GraphList)
    return graphs


@app.get("/graph/{graph_id}", response_model=GraphList)  # recover graph
async def get_graph(graph_id: str):
    graphs = await find_one_by_id(GraphList, graph_id)
    if graphs is None:
        raise HTTPException(
            status_code=404, detail=f"Graph {graph_id} not found")
    return graphs

# todo: request clarification about the last two endpoints
