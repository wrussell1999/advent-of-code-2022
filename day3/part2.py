with open('input.txt') as f:
    lines = f.readlines()

    sum = 0
    group_count = 0
    group = []
    for line in lines:
        group_count += 1
        group.append(line)
        if group_count == 3:
            group_count = 0
            for char in group[0]:
                if char in group[1] and char in group[2]:
                    if char.islower():
                        sum += (ord(char) - 96)
                        break
                    elif char.isupper():
                        sum += (ord(char) - 38)
                        break

            group.clear()

    print(sum)
