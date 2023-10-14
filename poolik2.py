lemmad_file = open("testid/wordlist.txt", "r", encoding="iso-8859-13")
lemmad = [line.strip().lower().replace("|", "") for line in lemmad_file]
lemmad_file.close()


def purify_word(word_1: str, word_2: str) -> str:
    if word_1 == word_2:
        return word_1

    leading1 = ""
    for char in word_1:
        if char.isalpha():
            break
        leading1 += char
    leading2 = ""
    for char in word_2:
        if char.isalpha():
            break
        leading2 += char
    leading = leading1 if len(leading1) <= len(leading2) else leading2

    if leading == word_1:
        return word_2
    elif leading == word_2:
        return word_1
    else:
        trailing1 = ""
        for char in word_1[::-1]:
            if char.isalpha():
                break
            trailing1 += char
        trailing2 = ""
        for char in word_2[::-1]:
            if char.isalpha():
                break
            trailing2 += char
        trailing = trailing1[::-1] if len(trailing1) <= len(trailing2) else leading2[::-1]
    #print("\"" + leading + "\", \"" + trailing + "\"")

    word_1a = "".join([char for char in word_1 if char.isalpha()])
    word_2a = "".join([char for char in word_2 if char.isalpha()])

    capitalised = (word_1a[0].isupper() if len(word_1a) else False) or (word_2a[0].isupper() if len(word_2a) else False)

    matches = [(match.capitalize() if capitalised else match) + "|" for match in find_lemmad_matches(word_1a, word_2a)]

    #print(word_1, word_2, "".join(matches).strip("|"))
    if len(matches) == 0:
        print(word_1, word_2)
        return word_1 + word_2 + "?????!!!!!!!"
    return leading + "".join(matches).strip("|") + trailing

def find_lemmad_matches(word_1: str, word_2: str) -> list[str]:
    word_1 = word_1.lower()
    word_2 = word_2.lower()

    matches = []

    for word in lemmad:
        vowels = get_vowels(word)
        consonants = get_consonants(word)
        if(consonants == word_1 and vowels == word_2): matches.append(word)

    return matches

def get_vowels(string: str) -> str:
    return "".join([char for char in string if char in "aeiouõäöü"])

def get_consonants(string: str) -> str:
    return "".join([char for char in string if char.isalpha() and not char in "aeiouõäöü"])

def fix_file(index: int, encoding: str):
    lines: list[str] = []
    try:
        file = open("testid/input_00" + str(index) + ".txt", "r", encoding=encoding)
        for line in file:
            lines.append(line)
    except UnicodeDecodeError:
        print("juhtus kala: " + str(index))
        return
    
    print("starting file: " + str(index))
    new_file = open("testid/output_00" + str(index) + ".txt", "w", encoding=encoding)
    for i in range(int(len(lines)/2)):
        words_1 = (lines[i]).split(" ")
        words_2 = (lines[int(len(lines)/2) + i]).split(" ")
        new_line = ""
        #print(words_1, words_2)
        for j in range(len(words_1)):
            word_1 = words_1[j]
            word_2 = words_2[j]
            new_line += purify_word(word_1, word_2) + " "
        new_line = new_line.strip(" ")
        new_file.write(new_line)
        print("line " + str(i) + " comlete")
        
    new_file.close()
    file.close()

fix_file(5, "utf-8")

#0 utf-8
#1 iso-8859-13
#2 cp850
#3 utf-8
#4 utf-8, wordlist
#5
#6
#7
#8
#9