from random import choice


def start_game():
    # Var List
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
        user_difficulty = int(input("\nPick your difficulty: [1,2,3]"))
        continue
    print(f"\nYou selected the: {difficulty_map[user_difficulty]} wordlist, good luck!")

    # Pick a word based using random.choice and user selection
    if user_difficulty == 1:
        game_wordlist = choice(easy_list)
    elif user_difficulty == 2:
        game_wordlist = choice(average_list)
    else:
        game_wordlist = choice(insane_list)
    return game_wordlist


# Test input
print(start_game())

# More to follow, this was just the first function.
