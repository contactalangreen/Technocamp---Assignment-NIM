
---

# NIM Champion: Token Takedown Arena

A fun, interactive Python implementation of the classic NIM game! Play head-to-head against a friend or challenge the computer in a battle of wits and strategy. 🪙⚔️

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Game Rules](#game-rules)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Example Gameplay](#example-gameplay)
- [Customization](#customization)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**NIM Champion: Token Takedown Arena** is a terminal-based Python game where players take turns removing tokens from piles. The player who takes the last token wins! The game supports both single-player (vs. computer) and two-player (local multiplayer) modes, with a user-friendly interface and emoji-powered visuals.

---

## Features

- 🎮 **Single-player**: Play against a computer opponent with random moves.
- 👥 **Multiplayer**: Challenge a friend in local head-to-head mode.
- 🥞 **Customizable piles**: Choose 1–5 piles, each with 1–10 tokens.
- 🪙 **Visual feedback**: See piles and tokens displayed with emojis.
- ⚠️ **Input validation**: Friendly prompts and error messages for invalid input.
- 🏆 **Victory celebration**: Winner is announced with a trophy!

---

## Game Rules

📜 **TOKEN RULES**
1. On your turn, take at least 1 token from **one** pile only.
2. You cannot empty a pile unless it has exactly 1 token left.
3. The player who takes the **last token** wins! 🏆
4. Every move counts… play bold, play smart!

---

## Installation

1. **Clone the repository or download the script:**
    ```bash
    git clone https://github.com/yourusername/nim-champion.git
    cd nim-champion
    ```

2. **(Optional) Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Run the game:**
    ```bash
    python nim.py
    ```

*No external dependencies required. Works with Python 3.7+.*

---

## How to Play

1. **Start the game**: Run `python nim.py` in your terminal.
2. **Choose game mode**: Select multiplayer (1) or singleplayer (2).
3. **Enter player names**: Input your name(s) as prompted.
4. **Set up piles**: Choose the number of piles (1–5) and tokens per pile (1–10).
5. **Take turns**: On your turn, select a pile and the number of tokens to remove (following the rules).
6. **Win the game**: The player who takes the last token is declared the winner!

---

## Example Gameplay

```
🚀  NIM CHAMPION: Token Takedown Arena!  🪙 ⚡

Good evening, strategist!
2025-11-16 20:15:42 PM GMT

📜  TOKEN RULES
1. Take at least 1 token from ONE pile only
2. You cannot empty a pile — unless it has exactly 1 token left
3. Snatch the last token → YOU WIN!  🏆
4. Every move counts… play bold, play smart! 

🚀  Ready to dominate?
Let's ignite the showdown! 

⚔️  CHOOSE YOUR BATTLE MODE!  ⚔️

Multiplayer (1): Duel a friend — head-to-head token chaos!
Singleplayer (2): Challenge the ultimate NIM Computer!

⌨️  Type 1 for Multiplayer or 2 for Singleplayer 
⌨️  Your choice (1 or 2): 2
✅  Mode selected!

👤  Enter your first name, brave challenger: Alice
 ⚔️  Alice, you are up against the Computer! Let the game begin! 

🥞   Enter the number of piles (1–5): 3
  ✅   3 pile(s) created!

🪙  Enter tokens in pile 1 (1–10): 4
✅  Pile 1: 4 tokens added!

🪙  Enter tokens in pile 2 (1–10): 2
✅  Pile 2: 2 tokens added!

🪙  Enter tokens in pile 3 (1–10): 5
✅  Pile 3: 5 tokens added!

🚀  GAME START!

🥞  CURRENT PILES:
   Pile 1:  🪙  🪙  🪙  🪙  (4 tokens)
   Pile 2:  🪙  🪙  (2 tokens)
   Pile 3:  🪙  🪙  🪙  🪙  🪙  (5 tokens)

👤  Alice, it's your turn!
⌨️  Choose a pile (1-3): 3
⌨️  How many tokens from Pile 3 (1–4): 2
✅  Alice removes 2 token(s) from Pile 3.

💻  Computer chooses Pile 1 and removes 1 token(s).

... (game continues) ...

🏁  Game Over!  🏆  Alice takes the last token and wins! Congratulations!
```

---

## Customization

- **Change token or pile limits**: Edit the values in `get_number_of_piles()` and `get_all_pile_sizes()` to allow more or fewer piles/tokens.
- **Improve computer AI**: The computer currently plays randomly. You can enhance the `get_computer_move()` function for smarter strategies.
- **Add new features**: Consider adding score tracking, undo moves, or graphical interfaces!

---

## Code Structure

- **nim.py**: Main game script containing all logic, user interaction, and game loop.
    - `main()`: Orchestrates the game flow.
    - `welcome_message()`: Prints intro and rules.
    - `choose_opponent()`: Selects game mode.
    - `get_player_names()`: Gets and validates player names.
    - `get_number_of_piles()`, `get_all_pile_sizes()`: Set up the game board.
    - `display_piles()`: Shows current piles and tokens.
    - `get_player_move()`, `get_computer_move()`: Handle player and computer turns.
    - `is_game_over()`: Checks for end of game.
    - `play_nim_game()`: Main game loop.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -am 'Add new feature'`
4. Push to your fork: `git push origin feature/your-feature`
5. Open a pull request describing your changes.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

Enjoy the game! 🚀  
Questions or suggestions? Open an issue or submit a pull request.

---

Would you like to add badges, a changelog, or further customization to your README? Let me know if you need additional sections or help!
