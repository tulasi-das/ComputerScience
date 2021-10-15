import random
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while "-" or " " in word:
        word = random.choice(word)
    
