import datetime
from playwright.sync_api import sync_playwright

def scrape_fanduel_odds():
    url = "https://sportsbook.fanduel.com/navigation/nba"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)

        # Wait for NBA game blocks to load (you may adjust selector based on actual layout)
        page.wait_for_selector('[data-test-id="event"]', timeout=15000)

        odds_data = []
        events = page.query_selector_all('[data-test-id="event"]')

        for event in events[:5]:  # Limit for MVP testing
            try:
                teams = event.query_selector_all('[data-test-id="team-name"]')
                odds = event.query_selector_all('[data-test-id="moneyline"]')

                if len(teams) == 2 and len(odds) == 2:
                    team_1 = teams[0].inner_text().strip()
                    team_2 = teams[1].inner_text().strip()

                    odds_1 = odds[0].inner_text().strip().replace("+", "")
                    odds_2 = odds[1].inner_text().strip().replace("+", "")

                    # Convert American odds to decimal
                    def to_decimal(american):
                        val = int(american)
                        return round((val / 100 + 1) if val > 0 else (100 / abs(val) + 1), 2)

                    game_id = f"{team_1}@{team_2}_{datetime.datetime.utcnow().date()}"

                    odds_data.extend([
                        {
                            "bookmaker": "FanDuel",
                            "sport": "NBA",
                            "league": "NBA",
                            "game_id": game_id,
                            "team_1": team_1,
                            "team_2": team_2,
                            "market": "moneyline",
                            "selection": team_1,
                            "odds_decimal": to_decimal(odds_1),
                            "timestamp": datetime.datetime.utcnow()
                        },
                        {
                            "bookmaker": "FanDuel",
                            "sport": "NBA",
                            "league": "NBA",
                            "game_id": game_id,
                            "team_1": team_1,
                            "team_2": team_2,
                            "market": "moneyline",
                            "selection": team_2,
                            "odds_decimal": to_decimal(odds_2),
                            "timestamp": datetime.datetime.utcnow()
                        }
                    ])
            except Exception as e:
                print("Skipping event due to error:", e)
                continue

        browser.close()
        return odds_data
