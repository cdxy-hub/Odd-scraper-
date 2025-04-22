import React from 'react'
import { useEffect, useState } from 'react'
import Bets from './Bets'

function App() {
  const [odds, setOdds] = useState([])

  useEffect(() => {
    fetch('http://localhost:8000/api/odds?sport=NBA&market=moneyline')
      .then(res => res.json())
      .then(data => setOdds(data))
      .catch(err => console.error(err))
  }, [])

  return (
    <div style={{ padding: '2rem' }}>
      <h1>NBA Moneyline Odds</h1>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Bookmaker</th>
            <th>Teams</th>
            <th>Selection</th>
            <th>Odds (Decimal)</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {odds.map((item, idx) => (
            <tr key={idx}>
              <td>{item.bookmaker}</td>
              <td>{item.team_1} vs {item.team_2}</td>
              <td>{item.selection}</td>
              <td>{item.odds_decimal}</td>
              <td>{new Date(item.timestamp).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <Bets />
    </div>
  )
}

export default App
