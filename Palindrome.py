def palin(word):
    if word == word[::-1]:
        return True
    else:
        return False

es_pali = print(palin("neuquen"))
