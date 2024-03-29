import random
import config
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def pick_random_word():
    return random.choice(FIVE_LETTER_WORDS)

def update_key_colors(gw, letter, color):
    current_color = gw.get_key_color(letter)
    if current_color == config.CORRECT_COLOR:
        return  # Don't downgrade color
    if current_color == config.PRESENT_COLOR and color == config.MISSING_COLOR:
        return  # Don't downgrade color
    gw.set_key_color(letter, color)

def color_boxes_and_keys(gw, guess, word, row):
    used_letters = [False] * len(word)
    # First pass for correct letters
    for col, letter in enumerate(guess):
        if word[col] == letter:
            gw.set_square_color(row, col, config.CORRECT_COLOR)
            update_key_colors(gw, letter.upper(), config.CORRECT_COLOR)
            used_letters[col] = True

    # Second pass for present and missing letters
    for col, letter in enumerate(guess):
        if gw.get_square_color(row, col) != config.CORRECT_COLOR:
            if letter in word and not used_letters[word.index(letter)]:
                gw.set_square_color(row, col, config.PRESENT_COLOR)
                update_key_colors(gw, letter.upper(), config.PRESENT_COLOR)
                used_letters[word.index(letter)] = True
            else:
                gw.set_square_color(row, col, config.MISSING_COLOR)
                update_key_colors(gw, letter.upper(), config.MISSING_COLOR)

def enter_action(gw, s):
    s = s.lower()  # Convert the entered word to lowercase
    if s in [word.lower() for word in FIVE_LETTER_WORDS]:  # Convert all words to lowercase for comparison
        gw.show_message("Word is a valid English word!")
        current_row = gw.get_current_row()
        color_boxes_and_keys(gw, s, random_word.lower(), current_row)
        if s == random_word.lower():
            gw.show_message("Congratulations, you guessed the word!")
        else:
            gw.set_current_row(current_row + 1)
    else:
        gw.show_message("Not in word list")

def wordle():
    global random_word

    config.colorblind_mode = input("Enable colorblind mode? (yes/no): ").lower().startswith('y')

    if config.colorblind_mode:
        config.CORRECT_COLOR = config.CORRECT_COLOR_CB
        config.PRESENT_COLOR = config.PRESENT_COLOR_CB

    gw = WordleGWindow()
    gw.add_enter_listener(lambda s: enter_action(gw, s))  # Connect the enter_action to the keyboard input

    # Pick a random word and display it in the first row
    random_word = pick_random_word()

if __name__ == "__main__":
    wordle()
