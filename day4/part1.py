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
                #print(board, n)
                columns = list()
                for c in range(5):
                    for r in range(5):
                        columns.append(n[r*5+c])
                games.append(','.join(columns))
                board += 1
                #print(board, columns)

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

winner = None
for n in numbers:
    if winner is not None: break
    for i in range(len(games)):
        if winner is not None: break
        ii = i // 2
        board = games[i].split(',')
        try:
            index = board.index(n)
            board[index] = '-0'
            games[i] = ','.join(board)
            win = '-0,-0,-0,-0,-0'
            if re.findall(win, games[i]):
                for j in findall(win, games[i]):
                    c = games[i].count(',', 0, j)
                    if c % 5 == 0:
                        unmarked = [ int(x) for x in games[i].split(',') ]
                        print(ii, games[i])
                        print(int(n) * sum(unmarked))
                        winner = ii
                        break
        except:
            pass
