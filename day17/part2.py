
area = dict()
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if 'target area:' in line:
            tokens = line.replace(',', '').split()
            for t in tokens:
                if '=' in t:
                    d, v = t.split('=')
                    values = [int(i) for i in v.split('..')]
                    area.setdefault(d, tuple(values))

class Probe(object):
    def __init__(self, vx, vy):
        self._x = 0
        self._y = 0
        self._vx = int(vx)
        self._vy = int(vy)

    # repurpose call for movement
    def __call__(self):
        # position changes base of current velocity
        self._x += self._vx
        self._y += self._vy
        # velocity is reduced
        if self._vx > 0: self._vx -= 1
        self._vy -= 1
        # return position
        return (self._x, self._y)


max_y = dict()
for x in range(1, 400):
    for y in range(-400, 400):
        pos = (x, y)
        print(pos)
        p = Probe(x, y)

        _max_y = 0
        on_target = False
        while True:

            pos = p()
            _max_y = max(_max_y, pos[1])

            if pos[0] > area['x'][1]:
                break
            elif pos[1] < area['y'][0]:
                break
            if area['x'][0] <= pos[0] <= area['x'][1]:
                if area['y'][0] <= pos[1] <= area['y'][1]:
                    on_target = True
                    break

        if on_target:
            max_y.setdefault(_max_y, list()).append((x, y))

print(max_y)
print(sum([len(max_y[y]) for y in max_y]))