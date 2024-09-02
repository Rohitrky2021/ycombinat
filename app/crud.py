from app.models import PipelineData, Node, Edge  # Use absolute import
from typing import List, Optional
from pydantic import BaseModel
import networkx as nx
# import matplotlib.pyplot as plt

def parse_pipeline(pipeline: PipelineData):
    nodes = pipeline.nodes
    edges = pipeline.edges

    # Calculate the number of nodes and edges
    num_nodes = len(nodes)
    num_edges = len(edges)

    # Determine if the graph is a DAG
    is_dag = check_if_dag(nodes, edges)

    return {'num_nodes': num_nodes, 'num_edges': num_edges, 'is_dag': is_dag}

def check_if_dag(nodes: List[Node], edges: List[Edge]) -> bool:


    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes
    for node in nodes:
        G.add_node(node.id)

    # Add edges
    for edge in edges:
        G.add_edge(edge.source, edge.target)

    # Check if the graph is a DAG
    is_dag = nx.is_directed_acyclic_graph(G)

    return is_dag
