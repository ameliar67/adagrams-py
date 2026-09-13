from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    letters = ''
    drawn_letters = []
    numbers_drawn = []

    for letter, count in LETTER_POOL.items():
        letters += letter * count

    for i in range(10):
        number = randint(1, len(letters) - 1)
        while number in numbers_drawn:
            number = randint(1, len(letters) - 1)
        numbers_drawn.append(number)
        drawn_letters.append(letters[number])

    return drawn_letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass