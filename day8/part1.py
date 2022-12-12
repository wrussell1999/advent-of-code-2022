with open('input.txt') as f:
    lines = f.readlines()

    data = []

    
    total_visible = 0 
    for line in lines:
        row = list(map(int, list(line.strip())))
        data.append(row)
    
    total_visible += (len(data[0]) * 2) + (len(data) - 2) * 2
    
    for y, row in enumerate(data):
        if y != 0 and y != len(data) - 1:
            for x, item in enumerate(row):
                if x != 0 and x != len(row) - 1:
                    left = True
                    right = True
                    top = True
                    bottom = True

                    for x_check, row_item in enumerate(row):
                        if item <= row_item:
                            if x_check < x:
                                left = False
                            elif x_check > x:
                                right = False
                            

                    if left or right:
                        total_visible += 1
                    else:
                        if not left and not right:
                            for y_check, col_item in enumerate(data):
                                if item <= col_item[x] and y != y_check:
                                    if y_check < y:
                                        top = False
                                    elif y_check > y:
                                        bottom = False
                                    
                        if top or bottom:
                            total_visible += 1
                    #print(f"{x + 1}, {y + 1}")

    print(total_visible)
