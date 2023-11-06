def search(self, word):
    global words
    letters = set(word)

    for word in words:
        if all(letter in word for letter in word):
            return True

    return False