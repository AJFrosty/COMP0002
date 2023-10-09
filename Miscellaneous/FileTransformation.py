import os.path

def deleteWord(file, word):
    content = open(file, "r")
    info = content.read()
    content.close()

    info = info.replace(word, '')
    content = open(file, "w")
    content.write(info)
    content.close()

deleteWord("TextFile.txt", "is")
