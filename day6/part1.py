with open('input.txt') as f:
    input = f.readline()

    hold = []
    counter = 0
    for char in input:
        if len(hold) == 4:
            if len(hold) == len(set(hold)):
                break
            else:
                hold.pop(0)
        hold.append(char)
        counter += 1

    print(counter)