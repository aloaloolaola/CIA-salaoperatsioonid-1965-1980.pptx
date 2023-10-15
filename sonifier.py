file_num = 8
with open("sonic/input_00" + str(file_num) + ".txt", "r", encoding="utf-8") as input_file:
    content = [line for line in input_file]

if len(content) <2:
    print("no map!")
    raise RuntimeError

height, width = content[0].split()

content.remove(content[0])

pos = None

for i in range(len(content)):
    line = content[i]
    if "S" in line:
        pos = [line.find("S"), i]
        content[i] = line.replace("S", ".")

if not pos:
    print("start_pos not found")
    raise RuntimeError

solution = ""
history = [pos.copy()]

input_ = None
while input_ != "x":
    map = content.copy()
    map[pos[1]] = map[pos[1]][:pos[0]] + "S" + map[pos[1]][pos[0]+1:]
    for line in map:
        print(line, end="")
    print(solution)
    #print(history)
    input_ = input("")
    if len(input_) == 0:
        continue
    input_ = input_[0]

    if input_ == "w" and (solution == "" or solution[-1] != "D"):
        pos[1] = pos[1] - 1
        solution += "U"
    elif input_ == "a"and (solution == "" or solution[-1] != "R"):
        pos[0] = pos[0] - 1
        solution += "L"
    elif input_ == "s"and (solution == "" or solution[-1] != "U"):
        pos[1] = pos[1] + 1
        solution += "D"
    elif input_ == "d"and (solution == "" or solution[-1] != "L"):
        pos[0] = pos[0] + 1
        solution += "R"
    elif input_ == "z" and len(history) > 1:
        history = history[0: -1]
        solution = solution[0: -1]
        pos = history[-1].copy()
        continue
    else:
        continue
    history.append(pos.copy())

with open("sonic/output_00" + str(file_num) + ".txt", "w", encoding="utf-8") as output_file:
    output_file.write(solution)