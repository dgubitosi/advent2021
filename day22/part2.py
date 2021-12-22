
class Cuboid(object):
    def __init__(self, x, y, z, state=False):
        self._dimensions = (x, y, z)
        self._state = (state == True)
        self._volume = self.__len__('x') * self.__len__('y') * self.__len__('z')

    @property
    def dimensions(self):
        return self._dimensions

    @property
    def x(self):
        return self._dimensions[0]

    @property
    def y(self):
        return self._dimensions[1]

    @property
    def z(self):
        return self._dimensions[2]

    @property
    def volume(self):
        return self._volume

    def __len__(self, axis):
        xyz = ['x','y','z']
        if axis not in xyz:
            return 0
        return self._dimensions[xyz.index(axis)][1] - self._dimensions[xyz.index(axis)][0] + 1

    def __bool__(self):
        return self._state == True

    def __repr__(self):
        if self.__bool__():
            state = 'on'
        else:
            state = 'off'
        return f"x={self.x}, y={self.y}, z={self.y}, volume={self.volume}, state={state}"

with open('test2.txt') as f:
    lines = f.readlines()

cuboids = list()
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
        c = Cuboid(x, y, z, state)
        cuboids.append(c)

