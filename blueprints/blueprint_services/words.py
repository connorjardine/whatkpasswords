import random

def get_words(num_limit=10):
    file = open('static/words_innit.txt', 'r')
    words = file.read().splitlines()
    words = random.sample(words, num_limit)
    return words


