import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def pick_random_word():
    return random.choice(FIVE_LETTER_WORDS)

def display_word_in_first_row(gw, word):
    for col in range(N_COLS):
        gw.set_square_letter(0, col, word[col])

def enter_action(gw, s):
    s = s.lower()  # Convert the entered word to lowercase
    if s in [word.lower() for word in FIVE_LETTER_WORDS]:  # Convert all words to lowercase for comparison
        gw.show_message("Word is a valid English word!")
    else:
        gw.show_message("Not in word list")


def wordle():
    gw = WordleGWindow()
    gw.add_enter_listener(lambda s: enter_action(gw, s))  # Pass gw when adding the listener

    # Pick a random word and display it in the first row
    random_word = pick_random_word()
    display_word_in_first_row(gw, random_word)

if __name__ == "__main__":
    wordle()
