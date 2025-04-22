from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.models import OddsSnapshot
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/odds")
def get_odds(
    sport: str = Query(None),
    market: str = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(OddsSnapshot)
    if sport:
        query = query.filter(OddsSnapshot.sport == sport)
    if market:
        query = query.filter(OddsSnapshot.market == market)
    results = query.order_by(OddsSnapshot.timestamp.desc()).limit(50).all()
    return [
        {
            "bookmaker": row.bookmaker,
            "sport": row.sport,
            "league": row.league,
            "game_id": row.game_id,
            "team_1": row.team_1,
            "team_2": row.team_2,
            "market": row.market,
            "selection": row.selection,
            "odds_decimal": row.odds_decimal,
            "timestamp": row.timestamp.isoformat()
        } for row in results
    ]
