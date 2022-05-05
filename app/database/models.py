from typing import Optional, List
from odmantic import Field, Model, EmbeddedModel


class BaseGraph(EmbeddedModel):
    source: str = Field(...)
    target: str = Field(...)
    distance: int = Field(...)


class UpdateGraph(Model):
    source: Optional[str]
    target: Optional[str]
    distance: Optional[int]


class GraphList(Model):
    data: List[BaseGraph] = Field(...)

    class Config:
        collection = "graph"