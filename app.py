from fastapi import FastAPI
from services.roi_service import get_roi_by_country, get_roi_by_genre
from services.runtime_evolution_service import  get_runtime_evolution
from services.actor_network_service import get_actor_network

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "MiniApi"}

@app.get("/roi_by_country")
async def roi_by_country():
    return get_roi_by_country()

@app.get("/roi_by_genre")
async def roi_by_genre():
    return get_roi_by_genre()

@app.get("/runtime_evolution")
async def runtime_evolution():
    return get_runtime_evolution()

@app.get("/actor_network")
async def actor_network():
    return get_actor_network()

@app.get("/health")
async def health():
    return {"status": "ok"}