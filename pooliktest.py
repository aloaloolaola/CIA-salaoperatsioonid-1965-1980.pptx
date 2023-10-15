VOWELS = "aeiouõäöüáéíóúæ"

def remove_vowels(string: str):
    return "".join(char for char in string if not char.lower() in VOWELS)

def remove_consonants(string: str):
    return "".join(char for char in string if char.lower() in VOWELS or not char.isalpha())

def check_file(broken: list[str], original: list[str]):
    broken1 = []
    broken2 = []
    errors = 0
    for line in original:
        broken1.append(remove_vowels(line))
        broken2.append(remove_consonants(line))
    broken1.extend(broken2)
    for i in range(len(broken)):
        if not broken[i] == broken1[i]:
            errors += 1
            print(i, "\n", broken[i], "\n", broken1[i], "\n")
    return errors

file0 = open("testid/input_004.txt", "r", encoding="utf-8")
file1 = open("testid/output_004.txt", "r", encoding="utf-8")
content0 = [row for row in file0]
content1 = [row for row in file1]
file0.close()
file1.close()

print(str(check_file(content0, content1)) + " errors")