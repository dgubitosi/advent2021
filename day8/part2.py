
segment_mask = [
    '1110111', # 0
    '0010010', # 1
    '1011101', # 2
    '1011011', # 3
    '0111010', # 4
    '1101011', # 5
    '1101111', # 6
    '1010010', # 7
    '1111111', # 8
    '1111011', # 9
]

total = 0
with open('input.txt') as f:
    for line in f:
        patterns, output = line.strip().split('|')
        patterns = patterns.split()
        output = output.split()

        _one = set()
        _seven = set()
        _four = set()
        _eight = set()
        _fives = list()
        _sixes = list()
        for p in patterns:
            p = set(p)
            l = len(p)
            # 2 segments = 1
            if l == 2:
                _one = p
            # 3 segments = 7
            elif l == 3:
                _seven = p
            # 4 segments = 4
            elif l == 4:
                _four = p
            # 7 segments = 8
            elif l == 7:
                _eight = p
            # 5 segments = 2, 3, 5
            elif l == 5:
                _fives.append(p)
            # 6 segments = 0, 6, 9
            elif l == 6:
                _sixes.append(p)

        # find nitial segment choices
        segments = [None]*7
        segments[0] = _seven - _one # a/top
        segments[1] = _four - _one # b/top left
        segments[2] = _one # c/top right
        segments[3] = segments[1].copy() # d/middle
        segments[4] = _eight - set().union(_seven, _four) # e/bottom left
        segments[5] = segments[2].copy() # f/bottom right
        segments[6] = segments[4].copy() # g/bottom

        # find the 3 to get the middle and bottom
        #print(segments)
        for _set in _fives:
            d = _set - _seven
            if len(d) == 2:
                segments[3] &= d
                segments[6] &= d

        # find the 6 to get the top right and bottom right
        #print(segments)
        for _set in _sixes:
            d = _seven - _set
            if len(d) == 1:
                segments[2] &= d
                segments[5] -= d

        # reduce any left overs
        #print(segments)
        _singles = set().union(*[_s for _s in segments if len(_s) == 1])
        for i, _s in enumerate(segments):
            if len(_s) > 1:
                segments[i] -= _singles

        # double check everthing has been resolved
        #print(segments)
        _singles = set().union(*[_s for _s in segments if len(_s) == 1])
        if len(_singles) != 7:
            continue

        # convert the output to a number
        segments = [ s.pop() for s in segments ]
        decode = dict()
        for p in patterns:
            key = ''
            n = ['0']*7
            for c in sorted(p):
                key += c
                i = segments.index(c)
                n[i] = '1'
            n = "".join(n)
            decode[key] = segment_mask.index(n)
        #print(decode)

        value = ''
        for o in output:
            o = "".join(sorted(o))
            value += str(decode[o])
        print(output, value)
        total += int(value)

print(total)
