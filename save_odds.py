from sqlalchemy.orm import Session
from app.models.models import OddsSnapshot

def save_odds_batch(db: Session, odds_list: list):
    for item in odds_list:
        odds = OddsSnapshot(
            bookmaker=item["bookmaker"],
            sport=item["sport"],
            league=item["league"],
            game_id=item["game_id"],
            team_1=item["team_1"],
            team_2=item["team_2"],
            market=item["market"],
            selection=item["selection"],
            odds_decimal=item["odds_decimal"],
            timestamp=item["timestamp"]
        )
        db.add(odds)
    db.commit()
