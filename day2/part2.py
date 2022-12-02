ROCK_POINT = 1
PAPER_POINT = 2
SCISSOR_POINT = 3

LOST_POINT = 0
DRAW_POINT = 3
WON_POINT = 6

ROCKS = 'A'
PAPERS = 'B'
SCISSORS = 'C'

LOST = 'X'
DRAW = 'Y'
WON = 'Z'

with open('input.txt') as f:
    lines = f.readlines()

    xyz_score = 0

    for line in lines:
        round = line.strip().split()
        
        if round[0] == ROCKS and round[1] == WON:
            xyz_score += PAPER_POINT
            xyz_score += WON_POINT
        elif round[0] == ROCKS and round[1] == DRAW:
            xyz_score += ROCK_POINT
            xyz_score += DRAW_POINT
        elif round[0] == ROCKS and round[1] == LOST:
            xyz_score += SCISSOR_POINT
            xyz_score += LOST_POINT
        elif round[0] == PAPERS and round[1] == WON:
            xyz_score += SCISSOR_POINT
            xyz_score += WON_POINT
        elif round[0] == PAPERS and round[1] == DRAW:
            xyz_score += PAPER_POINT
            xyz_score += DRAW_POINT
        elif round[0] == PAPERS and round[1] == LOST:
            xyz_score += ROCK_POINT
            xyz_score += LOST_POINT
        elif round[0] == SCISSORS and round[1] == WON:
            xyz_score += ROCK_POINT
            xyz_score += WON_POINT
        elif round[0] == SCISSORS and round[1] == DRAW:
            xyz_score += SCISSOR_POINT
            xyz_score += DRAW_POINT
        elif round[0] == SCISSORS and round[1] == LOST:
            xyz_score += PAPER_POINT
            xyz_score += LOST_POINT

    print(xyz_score)
