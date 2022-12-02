lines = open("input.txt").read().strip().split('\n')

xyz_to_abc = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C',
}

move_to_int = {
        'A': 0,
        'B': 1,
        'C': 2
}

def find_outcome(your_move_int: int, his_move_int: int) -> str:
    if your_move_int == (his_move_int - 1) % 3:
        return 'lose'
    elif your_move_int == his_move_int:
        return 'draw'
    elif your_move_int == (his_move_int + 1) % 3:
        return 'win'
    
score = 0

for line in lines:
    his_move, strategic_choice = line.split(' ')
    your_move_int = move_to_int[xyz_to_abc[strategic_choice]]
    his_move_int = move_to_int[his_move]
    outcome = find_outcome(your_move_int, his_move_int)
    if outcome == 'win':
        score += 6 
    elif outcome == 'draw':
        score += 3 
    score += your_move_int + 1

print(score)
    
