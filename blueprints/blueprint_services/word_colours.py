import random


def colour_words(words, num_colours=3):
    colours = ['red', 'green', 'blue']
    colours = colours[:num_colours]
    coloured_words = [(i, random.choice(colours)) for i in words]
    print(coloured_words)
    return coloured_words

