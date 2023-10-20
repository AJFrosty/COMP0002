import os.path

file = input("Enter File Name/Path: ")

while not os.path.isfile(file):
    file = input("Enter File Name/Path: ")

word = input("What word/phrase you want deleted: ")

def deleteWord(file, word):
    content = open(file, "r")
    info = content.read()
    content.close()

    info = info.replace(word, '')
    content = open(file, "w")
    content.write(info)
    content.close()
    print("Done")

deleteWord(file, word)
