for i in range(10):
    filename = "input_00" + str(i) + ".txt"
    file = open("testid/" + filename, "r")
    lines = []
    try:
        for line in file:
            lines.append(line)
    except UnicodeDecodeError:
        print("juhtus kala: ", i)
    else:
        new_file = open("testid/" + "new_" + filename, "w")
        for i in range(int(len(lines)/2)):
            new_file.write(lines[i])
            new_file.write(lines[int(len(lines)/2) + i])