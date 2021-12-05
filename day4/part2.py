import re

def findall(p, s):
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

numbers = list()
games = list()
board = -1
row = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            if board > -1:
                # convert rows into cols
                n = games[board].split(',')
                columns = list()
                for c in range(5):
                    for r in range(5):
                        columns.append(n[r*5+c])
                games.append(','.join(columns))
                board += 1

            board += 1
            row = 0
            games.append('')
            continue
        if ',' in line:
            numbers.extend(line.split(','))
            continue
        if row > 0:
            games[board] += ','
        games[board] += ','.join(re.split('\s+',line))
        row += 1

winners = list()
for n in numbers:
    for i in range(len(games)//2):
        for j in [0,1]:
            if i in [ x[0] for x in winners ]: break
            k = i + j
            board = games[k].split(',')
            try:
                index = board.index(n)
                board[index] = '-0'
                games[k] = ','.join(board)
                win = '-0,-0,-0,-0,-0'
                if re.findall(win, games[k]):
                    for pos in findall(win, games[k]):
                        c = games[k].count(',', 0, pos)
                        if c % 5 == 0:
                            unmarked = [ int(x) for x in games[k].split(',') ]
                            score = int(n) * sum(unmarked)
                            print(i, games[k])
                            print(pos, c, score)
                            winners.append((i, score))
                            break
            except:
                pass

print(winners)