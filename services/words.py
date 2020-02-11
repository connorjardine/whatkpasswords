from random_word import RandomWords

r = RandomWords()

def get_words(num_limit=10):
    words = r.get_random_words(hasDictionaryDef="true", includePartOfSpeech="verb", minDictionaryCount=1, minLength=3, maxLength=6, limit=10)
    return words