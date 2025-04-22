from fastapi import APIRouter
from app.api.odds import router as odds_router
from app.api.bets import router as bets_router

router = APIRouter()
router.include_router(odds_router)
router.include_router(bets_router)

@router.get("/ping")
def ping():
    return {"status": "ok"}
