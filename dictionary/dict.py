from PyDictionary import PyDictionary

DICT = PyDictionary()

user = input(str("word: "))


def user_meaning():
    meaning = DICT.meaning(user)
    return meaning


print(user_meaning())
