with open('input.txt') as f:
    lines = f.readlines()

    stacks = {}
    items_dict = {}
    for line in lines:
        line_chunks = line.split()      
        
        if len(line_chunks) == 0:
            continue

        if "[" in line_chunks[0]:
            position = 1
            spaces = 0
            for item in list(line):
                if item != '\n' and position not in items_dict:
                    items_dict[position] = ""
                if item == ' ' and spaces < 3:
                    spaces += 1
                elif item == ' ' and spaces > 2:
                    items_dict[position] += item
                    position += 1
                    spaces = 0
                if item != ' ' and item != '\n':
                    items_dict[position] += item
                    if item == ']':
                        position += 1 
                        spaces = 0
            
        elif line_chunks[0] == "1":
            for number in line_chunks:
                stacks[int(number)] = []
            for item in items_dict:
                item_hold = ''
                for char in items_dict[item]:
                    if char == ']':
                        stacks[item].append(item_hold)
                        item_hold = ''
                    elif char != '' and char != '[':
                        item_hold += char
                stacks[item].reverse()
        elif line_chunks[0] == "move":
            line_chunks.remove("move")
            line_chunks.remove("from")
            line_chunks.remove("to")
            # process the numbers. 0 means how many to move. 1 means from where. 2 means where to
            counter = 0
            moving_list = []
            parts = list(map(int, line_chunks))
            while counter < parts[0]:
                moving_list.append(stacks[parts[1]].pop())
                counter += 1
                if counter == parts[0]:
                    moving_list.reverse()
                    for item in moving_list:
                        stacks[parts[2]].append(item.strip())
                        
                    
                

    answer = ''
    for stack in stacks:
        print(stacks[stack])
        answer += stacks[stack].pop()

    print(answer)