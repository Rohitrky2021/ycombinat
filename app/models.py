from pydantic import BaseModel
from typing import List, Optional

class NodeData(BaseModel):
    id: str
    nodeType: str

class NodePosition(BaseModel):
    x: float
    y: float

class Node(BaseModel):
    id: str
    type: str
    position: NodePosition
    data: NodeData
    width: int
    height: int
    selected: bool = False
    dragging: bool = False
    positionAbsolute: Optional[NodePosition] = None

class EdgeMarker(BaseModel):
    type: str
    height: str
    width: str

class Edge(BaseModel):
    source: str
    sourceHandle: str
    target: str
    targetHandle: str
    type: str
    animated: bool = False
    markerEnd: EdgeMarker

class PipelineData(BaseModel):
    nodes: List[Node]
    edges: List[Edge]
