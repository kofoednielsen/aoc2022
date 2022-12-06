datastream = open('input.txt').read().strip()

for i in range(14,len(datastream)):
    if len(set(datastream[i-14:i])) == 14:
        print(i)
        exit()
