file = open("testid/norse_original.txt", "r", encoding="utf-8")
content = [line.strip().lower().replace("AE", "æ").replace("DH", "ð").replace("i/", "í").replace("a/", "á").replace("o/", "ó").replace("o,", "ö").replace("u/", "ú").replace("e/", "é") for line in file]
file.close()

#print(">", content[-10:-1])
new_content = []
for i in range(len(content)):
    #print(content[i].split()[-1])
    word = content[i].split()[-1]
    if len(word) != 0 and not word.isdigit():
        new_content.append(word + "\n")
    else:
        pass
        #print(word)

#print(">", new_content[-10:-1])

file = open("testid/norse.txt", "w", encoding="utf-8")
for string in new_content:
    pass
    file.write(string)