from random import choice
import string

def start_game():
    start_user_health = 6
    start_round_tracker = 1
    user_difficulty = 0
    guessed_letters = ['none']
    difficulty_map = {1: "easy", 2: "average", 3: "insane"}
    easy_list = ["cat", "dog", "egg", "beef", "hand"]
    average_list = ["goodbye", "letter", "ground", "snow", "water"]
    insane_list = ["gizmo", "peekaboo", "zigzagging", "fluffiness", "pneumonia"]
    game_word_blank = []
    fully_matched = False
    game_over = False
    remove_health_tracker = True

    print("Welcome to Guess or Die")
    print("I will pick a word and you have 6 incorrect guesses to get it right or you die")
    print("\nGame difficulty:")
    for skill_number, skill_level in difficulty_map.items():
        print(f"{skill_number}: {skill_level}")
    while user_difficulty not in range(1, 4):
        user_difficulty = int(input("\nPick your difficulty [1,2,3]: "))
        continue
    print(f"\nYou selected the: {difficulty_map[user_difficulty]} wordlist, good luck!")
    if user_difficulty == 1:
        game_wordlist = list(choice(easy_list))
    elif user_difficulty == 2:
        game_wordlist = list(choice(average_list))
    else:
        game_wordlist = list(choice(insane_list))
    input("Press 'Enter' to start the game")
    game_word_blank = blank_maker(game_wordlist, game_word_blank)
    valid_letters = approved_letters()
    return game_wordlist, start_user_health, start_round_tracker, game_word_blank, valid_letters, guessed_letters, fully_matched, game_over, remove_health_tracker

def blank_maker(game_wordlist, game_word_blank):
    game_word_blank = game_wordlist.copy()
    for index, item in enumerate(game_word_blank):
        game_word_blank[index] = "_"
    return game_word_blank

def approved_letters():
    lower_letters = string.ascii_lowercase
    valid_letters = []
    for letter in lower_letters:
        valid_letters.append(letter)
    return valid_letters

def game_menu(game_word_blank, user_health, round_tracker, valid_letters, guessed_letters):
    valid_guess = False
    letter_tracker = guessed_letter_sorter(guessed_letters)
    print("\n***********************************************")
    print(f"ROUND:{round_tracker}")
    print(f"Player Health:{user_health}")
    blank_display = print(*game_word_blank, sep = "")
    print(f"Word: {blank_display}")
    print(f"Guessed Letters: {letter_tracker}")
    print("************************************************")
    while not valid_guess:
        user_letter_choice = input("Guess a letter:")
        for letter in valid_letters:
            if letter == user_letter_choice:
                valid_guess = True
                print(f"You selected the letter: {letter}")
                print("************************************************")
                letter_tracker_update = update_used_letters(guessed_letters, user_letter_choice)
                break
            else:
                continue
    return valid_letters,letter_tracker_update, user_letter_choice, game_word_blank

def guessed_letter_sorter(guessed_letters):
    fixed_guess_string = ",".join(sorted(guessed_letters))
    return fixed_guess_string

def  update_used_letters(guessed_letters, user_letter_choice):
    if guessed_letters[0] == 'none':
        guessed_letters[0] = user_letter_choice
    else:
        guessed_letters.append(user_letter_choice)
    return guessed_letters

def game_updates(round_tracker, letter_tracker_update, valid_letter, user_letter_choice,game_word_blank,game_wordlist, fully_matched, game_over, user_health, remove_health_tracker):
    round_tracker += 1
    remove_health_tracker = True
    guessed_letters == letter_tracker_update
    valid_letter = valid_letter_update(valid_letter, user_letter_choice)
    game_word_blank, fully_matched, remove_health_tracker = word_blank_update(game_wordlist, game_word_blank, user_letter_choice, fully_matched, remove_health_tracker)
    if remove_health_tracker == True:
        user_health -=1
    if fully_matched:
        print("\n************************************************")
        print("YOU WIN!")
        print("YOU GUESSED THE CORRECT WORD:")
        blank_display = print(*game_wordlist, sep="")
        print("************************************************")
        game_over = True
    if user_health == 0:
        print("\n************************************************")
        print("YOU DIED!")
        print("DID NOT GUESS THE CORRECT WORD:")
        blank_display = print(*game_wordlist, sep="")
        print("************************************************")
        game_over = True
    return round_tracker, guessed_letters, valid_letter, game_word_blank, fully_matched, game_over, user_health, remove_health_tracker

def valid_letter_update(valid_letters, user_letter_choice):

    for letter in valid_letters:
        if letter == user_letter_choice:
            valid_letters.remove(letter)
    return valid_letters

def word_blank_update(game_wordlist, game_word_blank, user_letter_choice, fully_matched, remove_health_tracker):
        for index, item in enumerate(game_wordlist):
            if user_letter_choice == game_wordlist[index]:
                game_word_blank[index] = user_letter_choice
                remove_health_tracker = False
        if game_word_blank == game_wordlist:
                fully_matched = True
        return game_word_blank, fully_matched, remove_health_tracker

game_wordlist, user_health, round_tracker, game_word_blank, valid_letters, guessed_letters, fully_matched, game_over, remove_health_tracker = (start_game())

while not game_over:
    valid_letters, letter_tracker_update, user_letter_choice, game_word_blank = game_menu(game_word_blank, user_health, round_tracker, valid_letters, guessed_letters)
    round_tracker, letter_tracker_update, valid_letters, game_word_blank, fully_matched, game_over, user_health, remove_health_tracker = game_updates(round_tracker,letter_tracker_update, valid_letters, user_letter_choice, game_word_blank, game_wordlist, fully_matched, game_over, user_health, remove_health_tracker)

