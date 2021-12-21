
players = list()
with open('input.txt') as f:
    for line in f:
        array = line.strip().split()
        players.append((int(array[-1]), 0))

c = 0
winner = None
while True:
    if winner is not None: break
    for p in range(len(players)):
        pos, score = players[p]
        dice = list()
        for j in range(3):
            c += 1
            roll = c % 100
            if not roll: roll = 100
            dice.append(roll)
        roll = sum(dice)
        pos = (pos + roll) % 10
        if not pos: pos = 10
        score += pos
        print(f'player={p}, rolls={c}, dice={dice}, pos={pos}, score={score}')
        players[p] = (pos, score)
        if score >= 1000: 
            winner = p
            break
print(players)
loser = int(not winner)
print(c * players[loser][1])