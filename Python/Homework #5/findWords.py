def isFromSameRow(word):
    rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
    for i in range(len(word) - 1):
        for row in rows:
            if word[i] in row and word[i + 1] not in row:
                return False
    return True

def findWords(words):
    return [word for word in words if isFromSameRow(word)]
