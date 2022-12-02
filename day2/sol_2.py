lines = open("input.txt").read().strip().split('\n')

xyz_to_outcome = {
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win',
}

move_to_int = {
        'A': 0,
        'B': 1,
        'C': 2
}

def find_desired_move(desired_outcome: str, his_move_int: int) -> str:
    if desired_outcome == 'win':
        return (his_move_int + 1) % 3
    elif desired_outcome == 'draw':
        return his_move_int
    elif desired_outcome == 'lose':
        return (his_move_int - 1) % 3
    
score = 0

for line in lines:
    his_move, xyz = line.split(' ')
    disired_outcome = xyz_to_outcome[xyz]
    his_move_int = move_to_int[his_move]
    your_move_int = find_desired_move(disired_outcome, his_move_int)
    if disired_outcome == 'win':
        score += 6 
    elif disired_outcome == 'draw':
        score += 3 
    score += your_move_int + 1

print(score)
    
