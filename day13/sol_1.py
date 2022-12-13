import json
lines = open('input.txt').read().split('\n')

pairs = []
pair = []
for line in lines:
    if not line:
        pairs.append(pair)
        pair = []
    else:
        pair.append(json.loads(line))
    
def is_in_order(pair):
    # cast to lists
    for x, y in zip(*pair):
        if all(isinstance(v, int) for v in [x,y]):
            if x < y:
                return True
            if x > y:
                return False
        else:
            in_order = is_in_order([v if isinstance(v, list) else [v] for v in [x,y]])
            if in_order != None:
                return in_order
    if len(pair[0]) < len(pair[1]):
        return True
    if len(pair[0]) > len(pair[1]):
        return False


print(sum([i+1 for i, _ in filter(lambda tup: is_in_order(tup[1]), enumerate(pairs))]))
