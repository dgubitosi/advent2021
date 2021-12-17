import sys

with open('input.txt') as f:
    h = f.read().strip()
    i = int(h, 16)
    b = format(i, '0>8b')

operators = [
    'add',     # 0
    'mult',    # 1
    'min',     # 2
    'max',     # 3
    'literal', # 4
    'gt',      # 5
    'lt',      # 6
    'eq'       # 7
]

def resolve(index=0):
    v = None
    p = packets[index]
    size = p['size']
    print(f'{index}:', p)
    t = p['type'][0]

    # literals
    if t == 4:
        v = p['value']
        print(f'{index}: {operators[t]} {v}')
        nextp = index + 1

    # sub-packets
    else:
        stack = list()
        p = packets[index]
        length = p['length'][0]
        count = p['value']
        text = f'{index}: resolving sub-packets: {count}'

        # packets
        if length:
            print(f'{text} packets')
            i = 0
            nextp = index + 1
            while i < count:
                if nextp >= len(packets): break
                a, np = resolve(nextp)
                stack.append(a)
                nextp = np
                i += 1
 
        # bits
        else:
            print(f'{text} bits')

            # true next packet is after the bit length
            i = index + 1
            bits = 0
            while True:
                if i >= len(packets): break
                bits += packets[i]['size']
                if bits > count: break
                i += 1
            nextp = i

            # resolve packets within the bit boundary
            i = index + 1
            while i < nextp:
                a, np = resolve(i)
                stack.append(a)
                i = np

        # conditions
        if t > 4:
            print(f'{index}: resolving condition operands')
            a = stack[0]
            b = stack[1]

            # gt
            print(f'{index}: {a} {operators[t]} {b}')
            if t == 5:
                v = int(a > b)
            # lt
            if t == 6:
                v = int(a < b)
            # eq
            if t == 7:
                v = int(a == b)

        # operations
        # t < 4
        else:
            print(f'{index}: {operators[t]}{stack}')
            if t == 0:
                v = sum(stack)
            if t == 1:
                v = 1
                for s in stack:
                    v *= s
            if t == 2:
                v = min(stack)
            if t == 3:
                v = max(stack)

    # return value and next packet index
    print(f'{index}: return {v}, next {nextp}')
    return v, nextp

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

        # packet end
        if packet:
            packet['size'] = pos - start
            packets.append(packet)
            index = len(packets)-1
            print(index, b[start:pos])
            print(index, pos, packet)

    except:
        pass

r = resolve()
print(r[0])