
count = 0
with open('input.txt') as f:
    for line in f:
        patterns, output = line.strip().split('|')
        patterns = patterns.split()
        output = output.split()
        for o in output:
            l = len(o)
            # 2 segments = 1
            # 3 segments = 7
            # 4 segments = 4
            # 7 segments = 8
            if l in [2, 3, 4, 7]:
                count += 1
print(count)