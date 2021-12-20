
numbers = '0123456789'

with open('input.txt') as f:
    result = ''
    for line in f:
        s = line.strip()
        if not result:
            result = s
            continue
        print(' ', result)
        print('+', s)
        result = f'[{result},{s}]'
        print('=', result)
        print()

        _acted = True
        iteration = 0
        while _acted:
            iteration += 1
            print(iteration, result)
            _acted = False

            # explode
            pos = 0
            pair = [ '', '' ]
            _right = False
            _open = list()
            while pos < len(result):
                if _acted:
                    break

                c = result[pos]
                if c in numbers:
                    pair[int(_right)] += c

                elif c in '[]':
                    if c == ']':
                        # explode!
                        if pair[0] and pair[1] and len(_open) > 4:
                            _acted = True

                            left = pair[0]
                            right = pair[1]
                            pair_str = f'[{left},{right}]'
                            start = _open[-1]
                            end = pos + 1
                            print(iteration, 'explode', pair, "@", start, end)
                            result = result[:start] + '0' + result[end:]

                            # find number to the left
                            n = ''
                            j = start - 1
                            while j >= 0:
                                if result[j] in numbers:
                                    n = result[j] + n
                                elif n:
                                    #print(iteration, 'left', n)
                                    nn = str(int(n) + int(left))
                                    loc = j + 1
                                    #print(result[:loc])
                                    #print(nn)
                                    #print(result[loc+len(n):])
                                    result = result[:loc] + nn + result[loc+len(n):]
                                    start += 1
                                    break
                                j -= 1

                            # find number to the right
                            n = ''
                            j = start + 1
                            while j < len(result):
                                if result[j] in numbers:
                                    n += result[j]
                                elif n:
                                    #print(iteration, 'right', n)
                                    nn = str(int(n) + int(right))
                                    loc = j - len(n)
                                    #print(result[:loc])
                                    #print(nn)
                                    #print(result[loc+len(n):])
                                    result = result[:loc] + nn + result[loc+len(n):]
                                    break
                                j += 1

                            # explode complete
                            break

                        # not 4 deep yet
                        if _open:
                            _open.pop(-1)
                    
                    else:
                        _open.append(pos)

                    # reset state
                    pair = [ '', '' ]
                    _right = False

                # comma
                else:
                    _right =~ _right

                pos += 1

            # explode before split
            if _acted:
                continue

            # split
            n = ''
            pos = 0
            while pos < len(result):
                c = result[pos]
                if c in numbers:
                    n += c
                elif len(n) > 1:
                    _acted = True
                    print(iteration, 'split', n, "@", pos)
                    start = pos - len(n)
                    left = str(int(n) // 2)
                    right = str(int(n) // 2 + int(n) % 2)
                    pair_str = f'[{left},{right}]'
                    result = result[:start] + pair_str + result[pos:]
                    break
                else:
                    n = ''
                pos += 1

        print(result)

def magnitude(snailfish):

    if isinstance(snailfish, int):
        return snailfish

    if isinstance(snailfish, list):
        right = snailfish[1]
        left = snailfish[0]
        return 3 * magnitude(left) + 2 * magnitude(right)

print(magnitude(eval(result)))
