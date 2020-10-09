with open("test.txt") as file_obj:
    lines = 1
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line) - 1
        print(f"{letters} буквы в строке")
    print(f"Количество строк {lines}")
