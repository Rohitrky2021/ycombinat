from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import PipelineData  # Absolute import
from app.crud import parse_pipeline  # Absolute import

app = FastAPI()

# Add CORS Middleware
orig_origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://ycombinator1.vercel.app",
    "https://y-combina-front.vercel.app",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
def handle_pipeline(pipeline: PipelineData):
    return parse_pipeline(pipeline)



# python -m uvicorn app.main:app --reload

# python -m uvicorn app.main:app --reload