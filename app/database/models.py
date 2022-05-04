import collections
from typing import Optional, List
from odmantic import Field, Model, EmbeddedModel
from bson import ObjectId


class Graph(EmbeddedModel):
    source: str = Field(...)
    target: str = Field(...)
    distance: int = Field(...)


class UpdateGraph(Model):
    source: Optional[str]
    target: Optional[str]
    distance: Optional[int]

class GraphList(Model):
    data: List[Graph] = Field(...)

    class Config:
      collection = "graph"

if __name__ == "__main__":
    Graph
    GraphList
    UpdateGraph