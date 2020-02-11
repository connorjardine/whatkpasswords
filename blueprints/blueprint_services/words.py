import random


def get_words(num_limit=10, word_size='medium'):
    if word_size == 'medium':
        file = open('static/words_innit.txt', 'r')
    else:
        file = open('static/words_innit_large.txt', 'r')
    words = file.read().splitlines()
    words = random.sample(words, num_limit)
    return words


