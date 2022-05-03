from typing import List, Optional
from pydantic import BaseModel, Field

# the ObjectId needed for mongodb
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Graph(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    source: str
    target: str
    distance: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "source": "A",
                "target": "B",
                "distance": 1
            }
        }

class UpdateGraph(BaseModel):
    source: Optional[str]
    target: Optional[str]
    distance: Optional[int]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "source": "A",
                "target": "B",
                "distance": 1
            }
        }

class GraphList(BaseModel):
    data: List[Graph]

if __name__ == "__main__":
    GraphList
    UpdateGraph
    Graph
