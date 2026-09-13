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
    'AEIOULNRST': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
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
    letter_bank_copy = {}
    word = word.upper()

    for letter in letter_bank:
        if letter in letter_bank_copy:
            letter_bank_copy[letter]+=1
        else:
            letter_bank_copy[letter] = 1

    for letter in word:
        if letter not in letter_bank_copy:
            return False
        if letter_bank_copy[letter] > 0:
            letter_bank_copy[letter]-=1
        else:
            return False
    return True

def score_word(word):
    score = 0
    word = word.upper()
    if len(word) > 6 and len(word) < 11:
        score+=8

    for letter in word:
        for score_bracket in SCORES:
            for score_letter in score_bracket:
                if letter == score_letter:
                    score+=SCORES[score_bracket]

    return score

def get_highest_word_score(word_list):
    highest_score = 0
    highest_scoring_word = ''

    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            highest_scoring_word = word
        elif score == highest_score:
            if len(word) == 10 or len(word) < len(highest_scoring_word):
                if len(highest_scoring_word) != 10:
                    highest_scoring_word = word

    return (highest_scoring_word, highest_score)