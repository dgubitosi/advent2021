
with open('input.txt') as f:
    h = f.read().strip()
    i = int(h, 16)
    b = format(i, '0>8b')

packets = 0
sum_v = 0
pos = 0
while pos < len(b):
    start = pos
    try:
        packet = dict()
        v = int(''.join(b[pos:pos+3]), 2)
        sum_v += v
        pos += 3
        packet['version'] = v
        t = int(''.join(b[pos:pos+3]), 2)
        pos += 3

        # literal
        if t == 4:
            packet['type'] = (t, 'literal')
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
            packet['type'] = (t, 'operator')
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

        # packet end
        if packet:
            packet['size'] = pos - start
            packets += 1
            print(pos, packets, packet)

    except:
        pass

print(sum_v)