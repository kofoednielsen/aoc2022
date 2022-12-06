datastream = open('input.txt').read().strip()

for i in range(4,len(datastream)):
    if len(set(datastream[i-4:i])) == 4:
        print(i)
        exit()
