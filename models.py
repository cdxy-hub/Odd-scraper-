from sqlalchemy import Column, String, Float, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import datetime

Base = declarative_base()

class OddsSnapshot(Base):
    __tablename__ = "odds_snapshot"

    id = Column(Integer, primary_key=True, index=True)
    bookmaker = Column(String)
    sport = Column(String)
    league = Column(String)
    game_id = Column(String)
    team_1 = Column(String)
    team_2 = Column(String)
    market = Column(String)
    selection = Column(String)
    odds_decimal = Column(Float)
    timestamp = Column(TIMESTAMP, default=datetime.datetime.utcnow)

class UserBet(Base):
    __tablename__ = "user_bets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True))
    game_id = Column(String)
    selection = Column(String)
    odds_decimal = Column(Float)
    stake = Column(Float)
    result = Column(String)  # 'won', 'lost', 'pending'
    inserted_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
