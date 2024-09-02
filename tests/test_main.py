from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Ping': 'Pong'}

def test_parse_pipeline():
    pipeline = {
        "nodes": [
            {"id": "1", "type": "customInput", "position": {"x": 0, "y": 0}, "data": {"id": "1", "nodeType": "customInput"}, "width": 200, "height": 80},
            {"id": "2", "type": "text", "position": {"x": 1, "y": 1}, "data": {"id": "2", "nodeType": "text"}, "width": 200, "height": 80}
        ],
        "edges": [
            {"source": "1", "sourceHandle": "value", "target": "2", "targetHandle": "input", "type": "smoothstep", "animated": True, "markerEnd": {"type": "arrow", "height": "20px", "width": "20px"}}
        ]
    }
    response = client.post('/pipelines/parse', json=pipeline)
    assert response.status_code == 200
    assert response.json() == {'num_nodes': 2, 'num_edges': 1, 'is_dag': True}
