from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.models import UserBet
import uuid
import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class BetInput(BaseModel):
    game_id: str
    selection: str
    odds_decimal: float
    stake: float

@router.post("/bets")
def submit_bet(bet: BetInput, db: Session = Depends(get_db)):
    new_bet = UserBet(
        user_id=uuid.uuid4(),  # TODO: replace with real user system
        game_id=bet.game_id,
        selection=bet.selection,
        odds_decimal=bet.odds_decimal,
        stake=bet.stake,
        result="pending",
        inserted_at=datetime.datetime.utcnow()
    )
    db.add(new_bet)
    db.commit()
    db.refresh(new_bet)
    return {"status": "ok", "bet_id": new_bet.id}

@router.get("/bets")
def get_bets(db: Session = Depends(get_db)):
    bets = db.query(UserBet).order_by(UserBet.inserted_at.desc()).limit(50).all()
    return [
        {
            "game_id": b.game_id,
            "selection": b.selection,
            "odds_decimal": b.odds_decimal,
            "stake": b.stake,
            "result": b.result,
            "inserted_at": b.inserted_at.isoformat()
        } for b in bets
    ]
