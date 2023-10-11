import os.path

file = input("Enter File Name/Path: ")
if not os.path.isfile(file):
    raise NameError(f"The file: {file} does not exist!")

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
