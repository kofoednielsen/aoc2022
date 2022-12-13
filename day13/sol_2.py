import json
from functools import cmp_to_key
lines = open('input.txt').read().split('\n')

packets = []
for line in lines:
    if line:
        packets.append(json.loads(line))
    
packets.append([[2]])
packets.append([[6]])

def compare(x, y):
    # cast to lists
    for a, b in zip(x, y):
        if all(isinstance(v, int) for v in [a,b]):
            if a < b:
                return -1
            if a > b:
                return 1
        else:
            in_order = compare(*[v if isinstance(v, list) else [v] for v in [a,b]])
            if in_order != None:
                return in_order
    if len(x) < len(y):
        return -1
    if len(x) > len(y):
        return 1

sorted_packets = sorted(packets, key=cmp_to_key(compare))
for packet in sorted_packets:
    print(packet)

print((sorted_packets.index([[2]])+1) * (sorted_packets.index([[6]])+1))

