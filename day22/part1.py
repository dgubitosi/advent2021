

with open('input.txt') as f:
    lines = f.readlines()

init_area = dict()
for line in lines:
    #on x=10..12,y=10..12,z=10..12
    array = line.replace(',', ' ').split()
    state = None
    points = [None, None, None]
    for a in array:
        # state
        if a in ['on', 'off']:
            state = (a == 'on')
        # axis
        if '=' in a:
            axis, values = a.split('=')
            xyz = ['x','y','z']
            if axis in xyz:
                try:
                    # should have a list of two integers
                    points[xyz.index(axis)] = sorted([int(i) for i in values.split('..', 2)])
                except:
                    continue
    if state is not None:
        try:
            # should have three tuples
            x = tuple(points[0])
            y = tuple(points[1])
            z = tuple(points[2])
        except:
            continue
        in_init_area = True
        for p in points:
            if p[0] < -50 or p[1] > 50:
                in_init_area = False
                break
        if in_init_area:
            for xx in range(x[0], x[1]+1):
                for yy in range(y[0], y[1]+1):
                    for zz in range(z[0], z[1]+1):
                        loc = (xx, yy, zz)
                        init_area.setdefault(loc, False)
                        init_area[loc] = state

count = 0
for p in init_area:
    if init_area[p]:
        count += 1
print(count)