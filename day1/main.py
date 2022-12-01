with open('input.txt') as f:
    lines = f.readlines()
    max_cal = 0
    max_cals = []
    current_sum = 0

    for line in lines:
        if line.strip() == "":
            if current_sum > max_cal:
                max_cal = current_sum
            max_cals.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line.strip())

    max_cals.sort(reverse=True)
    while len(max_cals) > 3:
        del max_cals[len(max_cals) - 1]
    
    print(f"Top 3: {max_cals}. Total: {sum(max_cals)}")
