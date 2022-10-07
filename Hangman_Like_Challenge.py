from random import choice
import string


def start_game():
    # Var List
    start_user_health = 6
    start_round_tracker = 1
    user_difficulty = 0
    difficulty_map = {1: "easy", 2: "average", 3: "insane"}
    easy_list = ["cat", "dog", "egg", "beef", "hand"]
    average_list = ["goodbye", "letter", "ground", "snow", "water"]
    insane_list = ["gizmo", "peekaboo", "zigzagging", "fluffiness", "pneumonia"]

    # User menu, use difficulty_map to unpack choices
    print("Welcome to Guess or Die")
    print("I will pick a word and you have 6 incorrect guesses to get it right or you die")
    print("\nGame difficulty:")
    for skill_number, skill_level in difficulty_map.items():
        print(f"{skill_number}: {skill_level}")
    while user_difficulty not in range(1, 4):
        user_difficulty = int(input("\nPick your difficulty [1,2,3]: "))
        continue
    print(f"\nYou selected the: {difficulty_map[user_difficulty]} wordlist, good luck!")

    # Pick a word based using random.choice and user selection
    if user_difficulty == 1:
        game_wordlist = choice(easy_list)
    elif user_difficulty == 2:
        game_wordlist = choice(average_list)
    else:
        game_wordlist = choice(insane_list)
    input("Press 'Enter' to start the game")
    game_word_blank = blank_maker(game_wordlist)
    return game_wordlist, start_user_health, start_round_tracker, game_word_blank


def blank_maker(game_wordlist):
    game_word_blank = ""
    word_len_loop = 0
    while word_len_loop < len(game_wordlist):
        game_word_blank = game_word_blank + '-'
        word_len_loop += 1
    return game_word_blank


def game_menu(game_word_blank, user_health, round_tracker):
    valid_letters = approved_letters()
    valid_guess = False
    print("\n***********************************************")
    print(f"ROUND:{round_tracker}")
    print(f"Player Health:{user_health}")
    print(f"Word:{game_word_blank}")
    # NEED TO ADD USED LETTERS
    print("************************************************")
    while not valid_guess:
        user_letter_choice = input("Guess a letter:")
        for letter in valid_letters:
            if letter == user_letter_choice:
                valid_guess = True
                print(f"You selected the letter: {letter}")
                print("************************************************")
                break
            else:
                continue
    return valid_letters


def approved_letters():
    lower_letters = string.ascii_lowercase
    valid_letters = []
    for letter in lower_letters:
        valid_letters.append(letter)
    return valid_letters


# Test input
game_over = False
winning_word, user_health, round_tracker, game_word_blank = (start_game())

while not game_over:
    valid_letter = game_menu(game_word_blank, user_health, round_tracker)
    game_over = True
    # Make method that will compare letter, adjust blank, player health

# More to follow, this is an ongoing work in progress.
