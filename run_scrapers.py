from app.scrapers.fanduel import scrape_fanduel_odds
from app.services.save_odds import save_odds_batch
from app.db.session import SessionLocal

def run():
    session = SessionLocal()
    try:
        odds = scrape_fanduel_odds()
        save_odds_batch(session, odds)
        print(f"Saved {len(odds)} FanDuel odds.")
    finally:
        session.close()

if __name__ == "__main__":
    run()
