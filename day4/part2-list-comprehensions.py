numbers = list()
games = list()
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            games.append([])
            continue
        if ',' in line:
            numbers = [int(i) for i in line.split(',')]
            continue
        else:
            games[-1].extend([int(i) for i in line.split()])

winners = list()
for n in numbers:
    for i in range(len(games)):
        if i in [ x[0] for x in winners ]: continue
        game = games[i]
        try:
            index = game.index(n)
            game[index] = None
            rows = [ game[j:j+5] for j in range(0, len(game), 5) ]
            cols = [ game[j::5] for j in range(0, 5) ]
            for c in (rows + cols):
                if c.count(None) == 5:
                    score = n * sum([ int(j) for j in game if j is not None ])
                    winners.append((i, score))
                    break
        except:
            pass
print(winners)