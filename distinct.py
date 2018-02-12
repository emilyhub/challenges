# returns letters that don't overlap from word1 and word2
def distinct(word1, word2):
    letters = {}
    for letter in word1:
        letters[letter] = 1
    for letter in word2:
        if letter in letters:
            letters[letter] = 0
        else:
            letters[letter] = 2

    solution = []
    for k, v in letters.items():
        if v == 1 or v == 2:
            solution.append(k)

    return solution