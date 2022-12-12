with open('input.txt') as f:
    lines = f.readlines()

    data = []
    tree_scores = []
    temp = []
    
    total_visible = 0 
    for line in lines:
        row = list(map(int, list(line.strip())))
        data.append(row)

    for y, row in enumerate(data):
            if y != 0 and y != len(data) - 1:
                for x, item in enumerate(row):
                    left_counter = 0
                    right_counter = 0
                    up_counter = 0
                    down_counter = 0
                    if x != 0 and x != len(row) - 1:

                        # 2
                        x_left = x - 1
                        while x_left >= 0:
                            if item > row[x_left]:
                                left_counter += 1
                            elif item <= row[x_left]:
                                left_counter += 1
                                break
                            x_left -= 1
                        
                        # 2
                        x_right = x + 1
                        while x_right < len(row):
                            if item > row[x_right]:
                                right_counter += 1
                            elif item <= row[x_right]:
                                right_counter += 1
                                break
                            x_right += 1

                        # 2
                        y_up = y - 1
                        while y_up >= 0:
                            if item > data[y_up][x]:
                                up_counter += 1
                            elif item <= data[y_up][x]:
                                up_counter += 1
                                break
                            y_up -= 1
                        
                        # 1
                        y_down = y + 1
                        while y_down < len(data):
                            if item > data[y_down][x]:
                                down_counter += 1
                            elif item <= data[y_down][x]:
                                down_counter += 1
                                break
                            y_down += 1

                    tree_scores.append(left_counter * right_counter * up_counter * down_counter)

    print(max(tree_scores))