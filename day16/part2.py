
with open('input.txt') as f:
    h = f.read().strip()
    i = int(h, 16)
    b = format(i, '0>8b')

operators = [
    'sum',
    'product',
    'min',
    'max',
    'literal',
    'greater',
    'lesser',
    'equal'
]

packets = list()
pos = 0
while pos < len(b):
    start = pos
    try:
        packet = dict()
        v = int(''.join(b[pos:pos+3]), 2)
        pos += 3
        packet['version'] = v
        t = int(''.join(b[pos:pos+3]), 2)
        pos += 3
        packet['type'] = (t, operators[t])
        # literal
        if t == 4:
            value = ''
            while True:
                i = int(''.join(b[pos:pos+1]), 2)
                pos += 1
                value += ''.join(b[pos:pos+4])
                pos += 4
                if i == 0: break
            packet['value'] = int(value, 2)

        # operator
        else:
            l = int(''.join(b[pos:pos+1]), 2)
            pos += 1
            if l:
                # packets
                packet['length'] = (l, 'packets')
                l = 11
            else:
                # bits
                packet['length'] = (l, 'bits')
                l = 15
            packet['value'] = int(''.join(b[pos:pos+l]), 2)
            pos += l

    except:
        pass

    # packet end
    if packet:
        packet['size'] = pos - start
        packets.append(packet)
        print(pos, len(packets), packet)
