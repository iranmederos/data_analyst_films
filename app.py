from fastapi import FastAPI
from services.roi_service import get_roi_by_country, get_roi_by_genre
from services.runtime_service import  get_runtime_evolution
from services.correlation_service import get_budget_rating_corr

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

@app.get("/correlation/budget-rating")
async def actor_network():
    return get_budget_rating_corr()

@app.get("/health")
async def health():
    return {"status": "ok"}