# US States Game (Python Turtle + Pandas)

Guess all 50 U.S. states! Type the name of a state; if it’s correct, the game writes that state’s name on the map at the right location. Exit anytime to automatically generate a study file of the states you missed.

## 🎮 How to Play
- A prompt asks: “What’s another state?”
- Type a U.S. state’s full name (e.g., `California`, `New York`).
- Correct guesses are labeled on the map and counted.
- Type `exit` to stop early — the game creates `states_to_learn.csv` with the ones you missed.

> **Tip:** Input is normalized with `.title()`, so `texas`, `TEXAS`, and `Texas` are treated the same.


## 📦 Project Files
Place these files in the **same folder** (`US_States_Game/`):
- `main.py` — game script (your provided code)
- `50_states.csv` — dataset with columns: `state,x,y`
- `blank_states_img.gif` — background map image
- `README.md` — this file
- *(auto-generated)* `states_to_learn.csv` — created when you type `exit`

___
