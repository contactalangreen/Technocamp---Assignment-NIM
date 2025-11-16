from random import choice, randint
from datetime import datetime

'''
•  Part A: Displaying Two Token Piles [4 Marks]
•	Prompt the user to input two numbers, each representing the number of tokens in one of two piles.
•	Print a visual representation of these two token piles on the screen.
•	The display must clearly show the current state of both piles using tokens.

•  Part B: Two Pile Nim – Player vs Player [8 Marks]
•	Start by prompting for two numbers to set the initial sizes of the two token piles.
•	Implement a complete turn-based game between two human players (Player 1 and Player 2).
•	Before each player’s turn:
o	Display the current representation of both token piles.
o	Ask the current player:
	Which pile they want to remove tokens from.
	How many tokens they want to remove from that pile.
•	Validate every move:
o	Players cannot remove more tokens than are present in the chosen pile.
o	Players must remove at least one token.
•	Alternate turns between Player 1 and Player 2.
•	Continue until both piles are empty.
•	Declare the winner as the player who took the very last token.

•  Part C: Two Pile Nim – Player vs Computer [4 Marks]
•	Provide an option for the user to choose between playing against another human or against the computer.
•	If the user selects computer opponent:
o	Instead of prompting Player 2, the program automatically makes a move for the computer.
o	The computer must:
	Randomly select one of the non-empty piles.
	Randomly choose a valid number of tokens to remove (at least 1, up to the current size of the selected pile).
o	Display a clear message showing which pile the computer chose and how many tokens it removed.
•	Continue the game (human vs computer) with proper display before each turn.
•	When both piles are empty, announce the winner: either "player" or "computer".

•  Part D: Any Number of Piles Nim [4 Marks]
•	At the start, ask the user:
o	How many piles they want to play with (any positive integer).
o	The number of tokens for each individual pile (prompt separately for each).
•	Store the sizes of all piles in a list.
•	Implement the full Nim game with an arbitrary number of piles:
o	Players alternate turns (either Player 1 vs Player 2, or Player vs Computer based on earlier choice).
o	On each turn:
	Display the current state of all piles.
	Ask the current player (or compute for computer):
	Which pile to remove tokens from (must be a valid, non-empty pile).
	How many tokens to remove (valid range: 1 to current pile size).
o	Prevent invalid moves (e.g., choosing empty pile or removing too many tokens).
o	Continue until all piles are empty.
o	Declare the winner as the player (or computer) who took the last token.

•  Part E: Styling and Code Quality [5 Marks]
•	Follow consistent styling conventions used in class (indentation, spacing, etc.).
•	Use meaningful and appropriate variable names.
•	Include appropriate comments to explain logic where necessary.
•	Structure code to minimize repetition (avoid duplicated code blocks).
•	Present all output in a clean, clear, and user-friendly format.
•	Optional but beneficial: define and use functions to organize code.
o	If functions are used:
	All program logic must be inside functions.
	Include a main function.
	The only top-level statement should be the call to main().
•	A single, fully working program must be submitted that integrates all parts.

'''


# Global variables
token_icon = "🪙"
player1_name = ""
player2_name = ""
computer_name = "Computer"
pile_sizes = []
play_against_computer = False


def main():
    #welcome_message()
    choose_opponent()
    get_player_names()


def welcome_message():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p GMT")  # Get current date and time
    greeting = "Good morning, mastermind!" if "AM" in current_time else "Good evening, strategist!"  # Determine greeting based on time
    
    print(
        f"""🎉 NIM CHAMPION: Token Takedown Arena! 🪙 ⚡

        {greeting}
        {current_time}

        ⚡ TOKEN RULES
        1. Take at least 1 token from ONE pile only
        2. You cannot empty a pile — unless it has exactly 1 token left
        3. Snatch the last token → YOU WIN! 🏆
        4. Every move counts… play bold, play smart! 🔥+🧠

        🚀 Ready to dominate?
        Let's ignite the showdown! 💥"""
    )

def choose_opponent():
    # === Print the Game Mode Selection ===
    print(
        f"""
        🎮 CHOOSE YOUR BATTLE MODE! ⚔️ 🪙

        🔥 Multiplayer (1): Duel a friend — head-to-head token chaos!
        🤖 Singleplayer (2): Challenge the ultimate NIM Computer!

        ⚡ Type 1 for Multiplayer or 2 for Singleplayer 💥
        
        """
    )
    try:
        choice = int(input("Your choice (1 or 2): "))  # Get user input for game mode
        while choice not in [1, 2]:  # Validate input
            print("❌ Invalid choice. Please enter 1 or 2.")
            choice = int(input("Your choice (1 or 2): "))  # Re-prompt for valid input
    except ValueError:
        print("❌ Invalid input. Please enter a number (1 or 2).\n")
        choose_opponent()  # Restart function on invalid input
        return 
    global play_against_computer
    if choice == 1:
        play_against_computer = False
    elif choice == 2:
        play_against_computer = True
    

def get_player_names():
    if play_against_computer == True:
        while True:
            try:
                player1_name = input("Enter your first name, brave challenger: ").strip()
                if not player1_name:
                    raise ValueError("Player 1 name cannot be empty!")
                if not player1_name.isalpha():
                    raise ValueError("Only letters allowed for Player 1! No spaces or numbers.")

                player1_name = player1_name.lower().capitalize()
                player2_name = computer_name
                print(f"{player1_name}, you are up against the {computer_name}! Let the game begin! 🤖🎉")
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
                print("Please try again.\n")
    
    elif play_against_computer == False:
        while True:
            try:
                player1_name = input("Enter Player 1's first name: ").strip()
                if not player1_name:
                    raise ValueError("Player 1 name cannot be empty!")
                if not player1_name.isalpha():
                    raise ValueError("Only letters allowed for Player 1! No spaces or numbers.")

                player2_name = input("Enter Player 2's first name: ").strip()
                if not player2_name:
                    raise ValueError("Player 2 name cannot be empty!")
                if not player2_name.isalpha():
                    raise ValueError("Only letters allowed for Player 2! No spaces or numbers.")

                player1_name = player1_name.lower().capitalize()
                player2_name = player2_name.lower().capitalize()

                print(f"\n{player1_name} vs {player2_name}! Let the game begin! 🎉\n")
                break

            except ValueError as e:
                print(f"Invalid input: {e}")
                print("Please try again.\n")


    


def get_number_of_piles():
    pass


def get_all_pile_sizes(num_piles):
    pass


def display_piles(pile_sizes):
    pass


def get_player_move(player_name, pile_sizes):
    pass


def get_computer_move(pile_sizes):
    pass


def make_move(pile_sizes, pile_index, amount):
    pass


def is_game_over(pile_sizes):
    pass


def play_nim_game():
    pass



if __name__ == "__main__":
    main()




'''Program Characteristics 
•	Structure: Entire program built using functions; all logic inside functions; only top-level statement is main() call.
•	Control Flow:
o	for loops to avoid repetition (e.g., pile input, display, turn alternation).
o	while loops for input validation (keep asking until valid).
o	if statements with conditional operators for game logic and validation.
•	Data Types:
o	Lists to store pile sizes (dynamic number of piles).
o	No tuples or dictionaries needed (not ideal for this project – piles are ordered, mutable, and accessed by index).
o	Integers for pile counts, player choices, etc.
o	Strings for player names, messages, and formatted output.
•	Code Organisation:
o	Program clearly divided into Parts A–D with section comments.
o	Interconnections marked with inline comments in parentheses (e.g., # (Part B uses display_piles from Part A)).
•	Comments: Every line fully commented (purpose, not just restating code).
•	Naming Conventions:
o	Snake case for variables and functions (e.g., pile_sizes, get_player_move).
o	Descriptive, meaningful names (avoid x, temp, etc.).
o	Parameters follow same convention and clearly indicate purpose.
•	Output Formatting:
o	Use f-strings for clean, reusable formatted messages.
o	Wrap repeated formatting logic into functions (e.g., display_piles(), prompt_move()).
o	Consistent spacing: blank lines between logical blocks, aligned output.

•	Visuals:
o	Use a token emoji/icon (e.g., 🔴 or 🪙) to represent each token in a pile.
o	Piles displayed side-by-side with labels (e.g., Pile 1: 🔴🔴🔴).
•	User Experience:
o	Welcome message with game title, brief rules, and fun tone (emoji included).
o	Player names collected at start (Player 1, Player 2 or “Computer”).
o	All prompts use player names (e.g., “Alice, your turn!”).
o	Proactive, fun, friendly tone with emojis in messages (e.g., “Great move! 🎉”).
•	Language: British English (e.g., “initialise”, “tokens”, “behaviour”).
•	Error Handling:
o	try/except blocks around all user input to catch invalid types (non-integers).
o	Handle ValueError for non-numeric input.
o	Custom validation loops for out-of-range or invalid moves.
•	Terminal Only: No GUI, no OOP classes — pure procedural with functions.
________________________________________

Part A: Displaying Two Token Piles
Variables (local unless noted)
•	pile1_size → int (local)
•	pile2_size → int (local)
•	token_icon → str (global – reused across parts)
•	piles → list[int] (local, but will become global in later parts)
Functions
•	get_two_pile_sizes() → returns (pile1_size, pile2_size)
o	Parameters: none
o	(local variables only)
•	display_two_piles(pile1_size, pile2_size)
o	Parameters: pile1_size: int, pile2_size: int
o	(local variables only)
try/except Usage
•	In get_two_pile_sizes():
o	try/except ValueError when converting input to int
o	Loop with while True until valid positive integers
________________________________________

Part B: Two Pile Nim – Player vs Player
Variables (local unless noted)
•	pile1_size, pile2_size → int (local, from Part A)
•	current_player → str (local, alternates between player names)
•	player1_name, player2_name → str (global – set at start)
•	winner → str (local, set at game end)
•	move_pile, move_amount → int (local, per turn)
Functions
•	get_player_names() → returns (player1_name, player2_name)
o	(local input vars)
•	display_piles(pile_sizes) → replaces Part A version
o	Parameters: pile_sizes: list[int]
o	(local loop vars)
•	get_player_move(player_name, pile_sizes) → returns (pile_index, amount)
o	Parameters: player_name: str, pile_sizes: list[int]
o	(local: choice, amount, validation loop)
•	make_move(pile_sizes, pile_index, amount) → modifies list in place
o	Parameters: pile_sizes: list[int], pile_index: int, amount: int
o	(local: none)
•	is_game_over(pile_sizes) → returns bool
o	Parameters: pile_sizes: list[int]
o	(local: total_tokens)
•	play_two_pile_human_vs_human()
o	(local: all game loop vars)
try/except Usage
•	In get_player_move():
o	try/except ValueError for pile choice and amount input
o	Validate: pile index in range, pile not empty, amount ≥1 and ≤ pile size
________________________________________

Part C: Two Pile Nim – Player vs Computer
Variables (local unless noted)
•	play_against_computer → bool (local, from user choice)
•	computer_name → str = "Computer" (global)
•	computer_move → tuple (pile_index, amount) (local)
Functions
•	choose_opponent() → returns bool (True = vs computer)
o	(local input var)
•	get_computer_move(pile_sizes) → returns (pile_index, amount)
o	Parameters: pile_sizes: list[int]
o	(local: non_empty_piles list, random choice)
•	play_two_pile_player_vs_computer()
o	(local: current_player, move vars)
try/except Usage
•	In choose_opponent():
o	try/except ValueError for invalid input (not '1' or '2')
•	No try/except in get_computer_move() (uses list comprehension, safe)
________________________________________

Part D: Any Number of Piles Nim
Variables (local unless noted)
•	num_piles → int (local)
•	pile_sizes → list[int] (global – central game state)
•	player1_name, player2_name, computer_name → str (global)
•	play_against_computer → bool (global – affects turn logic)
•	current_player_index → int (local, 0 or 1)
•	last_mover → str (local, tracks who took last token)
Functions
•	get_number_of_piles() → returns num_piles: int
o	(local input var)
•	get_all_pile_sizes(num_piles) → returns pile_sizes: list[int]
o	Parameters: num_piles: int
o	(local loop var, input per pile)
•	display_piles(pile_sizes) → enhanced version
o	Parameters: pile_sizes: list[int]
o	(local: index, pile display string)
•	get_player_move(player_name, pile_sizes) → enhanced
o	Now accepts any number of piles
o	Validates pile index 1 to n
•	get_computer_move(pile_sizes) → enhanced
o	Chooses from any non-empty pile
•	play_nim_game() → main game loop
o	Integrates all logic
o	Alternates players (or player vs computer)
o	Uses for loop with modulo for turn order
o	Tracks last mover to declare winner
try/except Usage
•	In get_number_of_piles():
o	try/except ValueError, ensure ≥1
•	In get_all_pile_sizes():
o	try/except ValueError per pile input, ensure ≥0
•	In get_player_move() (enhanced):
o	try/except ValueError for pile index and amount
o	Validate pile index in range and pile not empty
________________________________________

Global vs Local Summary (in parentheses)
•	Global:
o	token_icon (str) – used in all display functions
o	player1_name, player2_name, computer_name (str) – set once, used everywhere
o	pile_sizes (list[int]) – central mutable game state (passed by reference)
o	play_against_computer (bool) – set once, controls game flow
•	Local:
o	All loop counters, temporary inputs, move choices, validation flags
o	Function-specific variables (e.g., non_empty_piles, total_tokens)
________________________________________
Main Function Structure
def main():
    # Welcome & setup
    # Choose opponent
    # Get player names
    # Get number of piles
    # Get pile sizes
    # Play game (calls play_nim_game)
    # Announce winner

All Parts Integrated
•	Part A → display_piles() (initial two-pile version)
•	Part B → play_two_pile_human_vs_human() (uses general functions)
•	Part C → play_two_pile_player_vs_computer() (uses same)
•	Part D → play_nim_game() (unifies all, supports n piles, both modes)
•	(Comment markers: # (Part A), # (Part B integration), etc.)
________________________________________

Error Handling Summary (try/except)
Location	                    Exception	                                Purpose
All int(input())	            ValueError	                                Non-numeric input
Pile index choice	            ValueError + range check	                Invalid pile number
Token amount	                ValueError + bounds check	                Invalid amount
Opponent choice	                ValueError	                                Not 1 or 2	
		
Extra: 
import random  # Required: Yes
# random.choice() → pick random non-empty pile
# random.randint() → pick random valid token count
'''