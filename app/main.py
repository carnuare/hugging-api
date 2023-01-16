from fastapi import FastAPI

from app.routers import testroute

app = FastAPI(title="Huggingface test API",
              description="This is a test API for Huggingface",
              version="0.0.1",
              contact={"name": "Carlos Núñez Arenas","email": "carnu@us.es"})

app.include_router(testroute.router, prefix="/test", tags=["huggingface"])
