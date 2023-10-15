file_num = 8
with open("sonic/cool_input_00" + str(file_num) + ".txt", "r", encoding="utf-8") as input_file:
    content = [line for line in input_file]

def construct_solution(content: list[str]) -> str:
    solution = ""
    pos = [1, 0]
    history = [pos.copy()]
    input_ = None
    while input_ != "x":
        map = content.copy()
        map[pos[1]] = map[pos[1]][:pos[0]] + "S" + map[pos[1]][pos[0]+1:]
        for line in map:
            print(line.replace("o", "+"), end="")
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
            if pos[1] > len(content) - 1:
                break
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

    return solution + "\n"

result = ""

unknown_lines = []
for line in content:
    if line[0] != "#":
        if(unknown_lines != []):
            result += construct_solution(unknown_lines)
            unknown_lines = []
        result += line
    else:
        unknown_lines.append(line)

with open("sonic/output_00" + str(file_num) + ".txt", "w", encoding="utf-8") as output_file:
    output_file.write(result.replace("\n", ""))