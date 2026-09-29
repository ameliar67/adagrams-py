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


SCORES = {
    'A': 1,
    'E': 1,
    'I': 1,
    'O': 1,
    'U': 1,
    'L': 1,
    'N': 1,
    'R': 1,
    'S': 1,
    'T': 1,
    'D': 2,
    'G': 2,
    'B': 3,
    'C': 3,
    'M': 3,
    'P': 3,
    'F': 4,
    'H': 4,
    'V': 4,
    'W': 4,
    'Y': 4,
    'K': 5,
    'J': 8,
    'X': 8,
    'Q': 10,
    'Z': 10
}

def draw_letters():
    letters = []
    drawn_letters = []
    numbers_drawn = []

    for letter, count in LETTER_POOL.items():
        letters += letter * count

    HAND_SIZE = 10

    for i in range(HAND_SIZE):
        number = randint(0, len(letters) - 1)
        while number in numbers_drawn:
            number = randint(0, len(letters) - 1)
        numbers_drawn.append(number)
        drawn_letters.append(letters[number])

    return drawn_letters

def uses_available_letters(word, letter_bank):
    letter_bank_copy = {}
    word = word.upper()

    for letter in letter_bank:
        letter_bank_copy[letter] = letter_bank_copy.get(letter, 0) + 1

    for letter in word:
        if letter_bank_copy.get(letter, 0) == 0:
            return False

        letter_bank_copy[letter] -= 1
    return True

def score_word(word):
    score = 0
    word = word.upper()
    LONG_WORD_BONUS_LENGTH_MIN = 7
    LONG_WORD_BONUS = 8
    if len(word) >= LONG_WORD_BONUS_LENGTH_MIN:
        score += LONG_WORD_BONUS

    for letter in word:
        score+=SCORES[letter]

    return score

def get_highest_word_score(word_list):
    highest_score = 0
    highest_scoring_word = ''
    words_with_highest_score = []

    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            highest_scoring_word = word
        elif score == highest_score:
             words_with_highest_score.append(word)

    if words_with_highest_score:
        for word in words_with_highest_score:
            if len(word) == 10 or len(word) < len(highest_scoring_word):
                if len(highest_scoring_word) != 10:
                    highest_scoring_word = word

    return (highest_scoring_word, highest_score)