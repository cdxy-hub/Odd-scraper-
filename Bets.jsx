import React, { useState, useEffect } from 'react'

export default function Bets() {
  const [bets, setBets] = useState([])
  const [form, setForm] = useState({
    game_id: '',
    selection: '',
    odds_decimal: '',
    stake: ''
  })

  useEffect(() => {
    fetch('http://localhost:8000/api/bets')
      .then(res => res.json())
      .then(setBets)
  }, [])

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    const res = await fetch('http://localhost:8000/api/bets', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ...form,
        odds_decimal: parseFloat(form.odds_decimal),
        stake: parseFloat(form.stake)
      })
    })
    if (res.ok) {
      alert("Bet saved!")
      setForm({ game_id: '', selection: '', odds_decimal: '', stake: '' })
      const updated = await fetch('http://localhost:8000/api/bets')
      setBets(await updated.json())
    }
  }

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Submit Bet Slip</h2>
      <form onSubmit={handleSubmit}>
        <input name="game_id" value={form.game_id} onChange={handleChange} placeholder="Game ID" required />
        <input name="selection" value={form.selection} onChange={handleChange} placeholder="Team" required />
        <input name="odds_decimal" value={form.odds_decimal} onChange={handleChange} placeholder="Odds (decimal)" required />
        <input name="stake" value={form.stake} onChange={handleChange} placeholder="Stake ($)" required />
        <button type="submit">Submit Bet</button>
      </form>

      <h2>Past Bets</h2>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Game</th>
            <th>Team</th>
            <th>Odds</th>
            <th>Stake</th>
            <th>Result</th>
            <th>Submitted</th>
          </tr>
        </thead>
        <tbody>
          {bets.map((b, i) => (
            <tr key={i}>
              <td>{b.game_id}</td>
              <td>{b.selection}</td>
              <td>{b.odds_decimal}</td>
              <td>{b.stake}</td>
              <td>{b.result}</td>
              <td>{new Date(b.inserted_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
