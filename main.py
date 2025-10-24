from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
from app.backend.routers.authentications import authentications
from app.backend.routers.users import users
from app.backend.routers.rols import rols

app = FastAPI(root_path="/api")
application = app

# FILES_DIR = "C:/Users/jesus/OneDrive/Desktop/escritorio/newerp/files"

# Montar como directorio estático
# app.mount("/files", StaticFiles(directory=FILES_DIR), name="files")

os.environ['SECRET_KEY'] = '7de4c36b48fce8dcb3a4bb527ba62d789ebf3d3a7582472ee49d430b01a7f868'
os.environ['ALGORITHM'] = 'HS256'

origins = [
    "*",
    "https://newerp-ghdegyc9cpcpc6gq.eastus-01.azurewebsites.net",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentications)
app.include_router(users)
app.include_router(rols)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        port=8000, 
        reload=True,
        timeout_keep_alive=1800,  # 30 minutos (30 * 60 = 1800 segundos)
        timeout_graceful_shutdown=60,  # 1 minuto para shutdown
        limit_max_requests=500000,  # 500,000 requests máximo
        limit_concurrency=500000,  # 500,000 concurrencia máxima
    )
