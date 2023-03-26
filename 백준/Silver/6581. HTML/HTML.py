answer, print_line = [], ""

while True:
    try:
        line = input().rstrip().split()

        for c in line:
            if c == "<br>":
                answer.append(print_line.strip())
                print_line = ""
            elif c == "<hr>":
                if print_line:
                    answer.append(print_line.strip())
                    print_line = ""
                answer.append("-" * 80)
            elif len(print_line) + len(c) >= 80:
                answer.append(print_line.strip())
                print_line = c + " "
            else:
                print_line += c + " "
    except:
        break
if print_line:
    answer.append(print_line.strip())
print(*answer, sep="\n")