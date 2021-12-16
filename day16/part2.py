
with open('input.txt') as f:
    h = f.read().strip()
    i = int(h, 16)
    b = format(i, '0>8b')

operators = [
    'add',   # 0
    'mult',  # 1
    'min',   # 2
    'max',   # 3
    '',      # 4
    'gt',    # 5
    'lt',    # 6
    'eq'     # 7
]

def resolve(index=0):
    v = None
    p = packets[index]
    print(f'{index}:', p)
    t = p['type'][0]
    # literal
    if t == 4:
        v = p['value']
        print(f'{index}: literal {v}')
    # conditions
    if t > 4:
        print(f'{index}: resolving condition operands')
        a = resolve(index + 1)
        b = resolve(index + 2)
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
    # stacks
    if t < 4:
        stack = list()
        length = p['length'][0]
        count = p['value']
        text = f'{index}: resolving stack, {count}'
        if length:
            # packets
            print(f'{text} packets')
            i = 1
            while i <= count:
                stack.append(resolve(index + i))
                i += 1
        else:
            # bits
            print(f'{text} packets')
            bits = 0
            i = index + 1
            while True:
                np = packets[i]
                bits += np['size']
                if bits > count: break
                stack.append(resolve(i))
                i += 1
        print(f'{index}: {operators[t]}({stack})')
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
    print(f'{index}: return {v}')
    return v

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
        print(len(packets)-1, pos, packet)

r = resolve()
print(r)