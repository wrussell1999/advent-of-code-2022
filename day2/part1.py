ROCK = 1
PAPER = 2
SCISSOR = 3

LOST = 0
DRAW = 3
WON = 6

ROCKS = ['A', 'X']
PAPERS = ['B', 'Y']
SCISSORS = ['C', 'Z']

with open('input.txt') as f:
    lines = f.readlines()

    xyz_score = 0

    for line in lines:
        round = line.strip().split()
        if round[1] in ROCKS:
            xyz_score += ROCK
        elif round[1] in PAPERS:
            xyz_score += PAPER
        elif round[1] in SCISSORS:
            xyz_score += SCISSOR
        
        if round[1] in ROCKS and round[0] in SCISSORS:
            xyz_score += WON
        elif round[1] in ROCKS and round[0] in ROCKS:
            xyz_score += DRAW
        elif round[1] in ROCKS and round[0] in PAPERS:
            xyz_score += LOST
        elif round[1] in PAPERS and round[0] in ROCKS:
            xyz_score += WON
        elif round[1] in PAPERS and round[0] in PAPERS:
            xyz_score += DRAW
        elif round[1] in PAPERS and round[0] in SCISSORS:
            xyz_score += LOST
        elif round[1] in SCISSORS and round[0] in PAPERS:
            xyz_score += WON
        elif round[1] in SCISSORS and round[0] in SCISSORS:
            xyz_score += DRAW
        elif round[1] in SCISSORS and round[0] in ROCKS:
            xyz_score += LOST

    print(xyz_score)
