with open('input.txt') as f:
    lines = f.readlines()

    sum = 0
    for line in lines:
        pair = line.strip().split(",")
        
        first = pair[0].split("-")
        second = pair[1].split("-")

        if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
            sum += 1
        elif int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
            sum += 1
        
    print(sum)