import json
lines = open('sample.txt').read().split('\n')

pairs = []
pair = []
for line in lines:
    if not line:
        pairs.append(pair)
        pair = []
    else:
        pair.append(json.loads(line))

for pair in pairs:
    print(pair)

def is_in_order(pair):
    # cast to lists
    print(f"comparing {pair[0]}, {pair[1]}")
    for x, y in zip(*pair):
        if all(isinstance(v, int) for v in [x,y]):
            print(f"comparing {x}, {y}")
            if x < y:
                print(f"✔️ {x} was smaller {y}")
                return True
            if x > y:
                print(f"❌ {x} was larger {y}")
                return False
        elif not is_in_order([v if isinstance(v, list) else [v] for v in [x,y]]):
                return False
    return len(pair[0]) <= len(pair[1])


print([i+1 for i, _ in filter(lambda tup: is_in_order(tup[1]), enumerate(pairs))])
