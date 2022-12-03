with open('input.txt') as f:
    lines = f.readlines()
    sum = 0

    for line in lines:
        compartment_1 = line[0:len(line)//2]
        compartment_2 = line[len(line)//2:len(line)]
        
        for char in compartment_1:
            if char in compartment_2:
                if char.islower():
                    sum += (ord(char) - 96)
                    break
                elif char.isupper():
                    sum += (ord(char) - 38)
                    break
    print(sum)
