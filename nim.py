# nim.py
# NIM Game: A two-player token removal game with single and multiplayer modes.


from random import choice, randint
# Imports the 'choice' function to randomly select one item from a list,
# and 'randint' to generate a random integer between two values.
# These are used for the computer's random moves.

from datetime import datetime
# Imports the 'datetime' class to work with dates and times,
# specifically to get the current time for the welcome message.

# === ICONS ===
COIN = " 🪙 "           # Token - Emoji string representing a single game token (coin).
PILE = " 🥞 "           # Pile marker - Emoji string used to mark or label piles of tokens.
PLAYER = " 👤 "       # Player turn - Emoji string indicating it's a human player's turn.
COMPUTER = " 💻 "   # Computer turn - Emoji string indicating it's the computer's turn.
TROPHY = " 🏆 "        # Winner - Emoji string used to celebrate the winning player.
WARNING = " ⚠️ "     # Error - Emoji string displayed for invalid inputs or errors.
ROCKET = " 🚀 "       # Start game - Emoji string used for game start and excitement.
SWORDS = " ⚔️ "       # Battle mode - Emoji string for battle/versus themes.
INPUT = " ⌨️ "         # Input prompt - Emoji string shown before user input prompts.
CHECK = " ✅ "         # Valid move - Emoji string confirming a successful/valid action.
GAME_OVER = " 🏁 " # Game end - Emoji string signalling the end of the game.
RULES = " 📜 "         # Rules icon - Emoji string used when displaying game rules.
VS = " ⚔️ "               # Versus - Emoji string for showing player vs player/computer.

# Global variables - These store game state accessible across all functions.
player1_name = ""                        # Stores the name of Player 1 (first human player).
player2_name = ""                        # Stores the name of Player 2 (second human or unused).
COMPUTER_NAME = "Computer"               # Fixed string name used for the computer opponent.
num_piles = 0                            # Integer tracking the total number of piles in the game.
pile_sizes = []                          # List holding the current number of tokens in each pile.
play_against_computer = False            # Boolean flag: True if playing single-player vs computer, False for multiplayer.

#
def welcome_message():
    # Displays a fancy welcome screen with rules, current time, and game intro.
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p GMT")
    # Gets the current date/time, formats it as "YYYY-MM-DD HH:MM:SS AM/PM GMT"
    # for display in the greeting.
    
    greeting = "Good morning, mastermind!" if "AM" in current_time else "Good evening, strategist!"
    # Sets a time-based greeting: "Good morning..." if AM, otherwise "Good evening...".

    print(
        f"""{ROCKET}  NIM CHAMPION: Token Takedown Arena!  {COIN} ⚡

        {greeting}
        {current_time}

        {RULES}  TOKEN RULES
        1. Take at least 1 token from ONE pile only
        2. You cannot empty a pile — unless it has exactly 1 token left
        3. Snatch the last token → YOU WIN!  {TROPHY}
        4. Every move counts… play bold, play smart! 

        {ROCKET}  Ready to dominate?
        Let's ignite the showdown! """
    )
    # Prints the multi-line welcome message using f-string with icons and variables.


def choose_opponent():
    # Prompts the user to select game mode: multiplayer or single-player vs computer.
    print(
        f"""
        {SWORDS}  CHOOSE YOUR BATTLE MODE!  {SWORDS}

        Multiplayer (1): Duel a friend — head-to-head token chaos!
        Singleplayer (2): Challenge the ultimate NIM Computer!

        {INPUT}  Type 1 for Multiplayer or 2 for Singleplayer """
    )
    # Displays the battle mode selection menu with options.
    
    try:
        choice = int(input(f"{INPUT}  Your choice (1 or 2): "))
        # Attempts to read and convert user input to an integer (1 or 2).
        
        while choice not in [1, 2]:
            # Loops until a valid choice (1 or 2) is entered.
            print(f"{WARNING}  Invalid choice. Please enter 1 or 2.")
            choice = int(input(f"{INPUT}  Your choice (1 or 2): "))
            # Reprompts for input inside the loop.
            
    except ValueError:
        # Catches non-integer inputs (e.g., letters or symbols).
        print(f"{WARNING}  Invalid input. Please enter a number (1 or 2).\n")
        choose_opponent()
        return
        # Recursively restarts the function for invalid input and exits current call.
    
    global play_against_computer
    # Declares use of the global 'play_against_computer' variable.
    
    play_against_computer = choice == 2
    # Sets the flag: True if choice is 2 (single-player), False if 1 (multiplayer).
    
    print(f"{CHECK}  Mode selected!\n")
    # Confirms the mode selection.


def get_player_names():
    # Collects and validates player names based on game mode.
    global player1_name, player2_name
    # Declares use of global player name variables.
    
    if play_against_computer:
        # Handles single-player mode (human vs computer).
        while True:
            # Loops until valid input.
            try:
                player1_name = input(f"{PLAYER}  Enter your first name, brave challenger: ").strip()
                # Reads and removes whitespace from player 1's name input.
                
                if not player1_name or not player1_name.isalpha():
                    # Checks if name is empty or contains non-letter characters.
                    raise ValueError("Name must contain only letters and cannot be empty.")
                    # Raises error for invalid names.
                
                player1_name = player1_name.lower().capitalize()
                # Formats name: lowercase then capitalise first letter (e.g., "John").
                
                player2_name = COMPUTER_NAME
                # Sets player 2 as the computer.
                
                print(f" {VS}  {player1_name}, you are up against the {COMPUTER_NAME}! Let the game begin! \n")
                # Announces the matchup.
                
                break
                # Exits loop on success.
                
            except ValueError as e:
                # Catches validation errors.
                print(f"{WARNING}  Invalid input: {e}\nPlease try again.\n")
                # Shows error and reprompts.
    
    else:
        # Handles multiplayer mode (two humans).
        while True:
            try:
                player1_name = input(f"{PLAYER}  Enter Player 1's first name: ").strip()
                # Gets Player 1 name.
                
                if not player1_name or not player1_name.isalpha():
                    raise ValueError("Player 1 name must contain only letters and cannot be empty.")
                    # Validates Player 1 name.

                player2_name = input(f"{PLAYER}  Enter Player 2's first name: ").strip()
                # Gets Player 2 name.
                
                if not player2_name or not player2_name.isalpha():
                    raise ValueError("Player 2 name must contain only letters and cannot be empty.")
                    # Validates Player 2 name.

                player1_name = player1_name.lower().capitalize()
                player2_name = player2_name.lower().capitalize()
                # Formats both names properly.
                
                print(f"\n {VS}  {player1_name} vs {player2_name}! Let the game begin! \n")
                # Announces the matchup.
                
                break
                # Exits loop on success.
                
            except ValueError as e:
                print(f"{WARNING}  Invalid input: {e}\nPlease try again.\n")
                # Shows error and reprompts.


def get_number_of_piles():
    # Prompts for and validates the number of piles (1-5).
    global num_piles
    # Declares use of global 'num_piles'.
    
    while True:
        # Loops until valid input.
        try:
            num_piles = int(input(f"{PILE}   Enter the number of piles (1–5): "))
            # Reads and converts input to integer.
            
            if 1 <= num_piles <= 5:
                # Checks if within allowed range.
                print(f"  {CHECK}   {num_piles} pile(s) created!\n")
                # Confirms selection.
                
                break
                # Exits loop.
                
            print(f"{WARNING}   Please enter a number between 1 and 5.")
            # Error for out-of-range.
            
        except ValueError:
            print(f"{WARNING}   Please enter a valid integer.")
            # Error for non-integer input.
    
    return num_piles
    # Returns the validated number (though global, for function completeness).


def get_all_pile_sizes(num_piles):
    # Collects and validates token sizes for each pile (1-10 tokens each).
    global pile_sizes
    # Declares use of global 'pile_sizes' list.
    
    pile_sizes = []
    # Initialises empty list for pile sizes.
    
    for i in range(num_piles):
        # Loops once per pile (i from 0 to num_piles-1).
        
        while True:
            # Inner loop for valid input per pile.
            try:
                size = int(input(f"{COIN}  Enter tokens in pile {i+1} (1–10): "))
                # Reads and converts tokens for current pile.
                
                if 1 <= size <= 10:
                    # Validates range.
                    pile_sizes.append(size)
                    # Adds size to the list.
                    
                    print(f"{CHECK}  Pile {i+1}: {size} tokens added!\n")
                    # Confirms addition.
                    
                    break
                    # Next pile.
                    
                print(f"{WARNING}  Please enter a number between 1 and 10.")
                # Range error.
                
            except ValueError:
                print(f"{WARNING}  Please enter a valid integer.")
                # Non-integer error.
    
    return pile_sizes
    # Returns the populated list.


def display_piles(pile_sizes):
    # Visually prints the current state of all piles with token emojis.
    print(f"\n{PILE}  CURRENT PILES:")
    # Header for piles display.
    
    for index, size in enumerate(pile_sizes):
        # Loops over each pile's index and size.
        
        display_size = max(0, size)
        # Ensures size is never negative (clamps to 0).
        
        tokens = (COIN + " ") * display_size
        # Creates string of '🪙 ' repeated for each token (plus space).
        
        status = "EMPTY" if display_size == 0 else f"{display_size} tokens"
        # Sets status text: "EMPTY" or "X tokens".
        
        print(f"   Pile {index + 1}: {tokens} ({status})")
        # Prints pile line with visual tokens and status.
    
    print()  # Extra line for clarity
    # Adds blank line after display for readability.


def get_player_move(player_name, pile_sizes):
    # Handles a human player's turn: selects pile and tokens to remove.
    print(f"{PLAYER}  {player_name}, it's your turn!")
    # Announces whose turn it is.
    
    while True:
        # Loops until valid complete move.
        try:
            pile_input = input(f"{INPUT}  Choose a pile (1-{len(pile_sizes)}): ").strip()
            # Gets pile number input, strips whitespace.
            
            pile_index = int(pile_input) - 1
            # Converts to 0-based index (user sees 1-based).

            if not (0 <= pile_index < len(pile_sizes)):
                # Checks if pile index is valid.
                print(f"{WARNING}  Please choose a pile between 1 and {len(pile_sizes)}.")
                continue
                # Reprompts for pile.

            current = pile_sizes[pile_index]
            # Gets current tokens in selected pile.
            
            if current <= 0:
                # Cannot choose empty pile.
                print(f"{WARNING}  That pile is empty. Choose another.")
                continue
                # Reprompts.

            if current == 1:
                # Special rule: must take the single last token.
                amount = 1
                print(f"{PILE}  You must take the last token from Pile {pile_index + 1}.")
                # Informs player.
            else:
                # Normal case: choose 1 to (current-1) tokens.
                max_allowed = current - 1
                # Cannot empty pile unless 1 token.
                
                amount_input = input(f"{INPUT}  How many tokens from Pile {pile_index + 1} (1–{max_allowed}): ").strip()
                # Prompts for amount.
                
                amount = int(amount_input)
                # Converts to int.
                
                if amount < 1 or amount > max_allowed:
                    # Validates amount.
                    print(f"{WARNING}  Please enter a number between 1 and {max_allowed}.")
                    continue
                    # Reprompts.

            # Apply move - This executes after validation.
            pile_sizes[pile_index] -= amount
            # Subtracts tokens from pile.
            
            if pile_sizes[pile_index] < 0:
                pile_sizes[pile_index] = 0
                # Clamps to 0 if somehow negative.

            print(f"{CHECK}  {player_name} removes {amount} token(s) from Pile {pile_index + 1}.\n")
            # Confirms the move.
            
            return pile_index, amount
            # Returns the pile index and amount removed for logging if needed.

        except ValueError:
            # Catches any non-numeric input.
            print(f"{WARNING}  Invalid input. Please enter numbers only.")
            # Reprompts.


def get_computer_move(pile_sizes):
    # Generates and applies the computer's random move.
    non_empty = [i for i, s in enumerate(pile_sizes) if s > 0]
    # Creates list of indices of piles with tokens (>0).
    
    pile_index = choice(non_empty)
    # Randomly selects one non-empty pile.
    
    current = pile_sizes[pile_index]
    # Gets tokens in chosen pile.

    if current == 1:
        amount = 1
        # Must take the last token.
    else:
        amount = randint(1, current - 1)
        # Randomly chooses 1 to (current-1) tokens.

    pile_sizes[pile_index] -= amount
    # Applies the move.
    
    if pile_sizes[pile_index] < 0:
        pile_sizes[pile_index] = 0
        # Clamps to 0.

    print(f"{COMPUTER}  {COMPUTER_NAME} chooses Pile {pile_index + 1} and removes {amount} token(s).\n")
    # Announces computer's move.
    
    return pile_index, amount
    # Returns details (though not used in main game loop).


def is_game_over(pile_sizes):
    # Checks if all piles are empty (or <=0).
    return all(s <= 0 for s in pile_sizes)
    # Returns True if every pile has no tokens left.
    # 'all()' with generator: True only if no tokens remain anywhere.


def play_nim_game(pile_sizes, player1_name, player2_name, play_against_computer):
    # Main game loop: alternates turns until game over.
    last_mover = None
    # Tracks who took the last token (the winner).
    
    turn = 0  # 0: player1, 1: player2/computer
    # Turn counter: even for player1, odd for player2/computer.

    print(f"{ROCKET}  GAME START!\n")
    # Kicks off the game.

    while not is_game_over(pile_sizes):
        # Continues until all piles empty.
        
        display_piles(pile_sizes)
        # Shows current board state before each turn.

        if play_against_computer and turn == 1:
            # Single-player and computer's turn.
            player_name = COMPUTER_NAME
            get_computer_move(pile_sizes)
            # Computer makes random move.
        else:
            # Human player's turn (player1 or player2).
            player_name = player1_name if turn == 0 else player2_name
            # Selects correct player name.
            
            get_player_move(player_name, pile_sizes)
            # Human makes move.

        last_mover = player_name
        # Records who just moved (potential winner).
        
        turn = 1 - turn
        # Flips turn: 0<->1 (alternates players).

    display_piles(pile_sizes)
    # Final board display (all empty).
    
    print(f"{GAME_OVER}  Game Over!  {TROPHY}  {last_mover} takes the last token and wins! Congratulations! \n")
    # Declares winner: whoever took the last token.


def main():
    # Orchestrates the entire game flow from start to finish.
    welcome_message()
    # Shows intro and rules.
    
    choose_opponent()
    # Selects game mode.
    
    get_player_names()
    # Gets player names.
    
    get_number_of_piles()
    # Sets number of piles.
    
    get_all_pile_sizes(num_piles)
    # Sets sizes for each pile.
    
    play_nim_game(pile_sizes, player1_name, player2_name, play_against_computer)
    # Runs the core game loop.


if __name__ == "__main__":
    main()
    # Standard Python idiom: runs main() only if script executed directly (not imported).
