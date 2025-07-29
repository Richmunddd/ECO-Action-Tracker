import sys
import os
from pathlib import Path
from fastapi import FastAPI

# Add project root to Python path
sys.path.append(str(Path(__file__).parent.parent))

from business_layer.api import router

app = FastAPI()
app.include_router(router)

# app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
