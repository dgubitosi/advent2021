

def Reduce(snailfish, depth=0):

    # custom error to capture action, Explode or Reduce
    class _Action(Exception):
        def __init__(self, action, value, depth):
            self.action = action
            if self.action == 1:
                self.text = 'Explode'
            if self.action == 2:
                self.text = 'Split'
            self.value = value
            self.depth = depth
            self.message = f"{self.text} {self.value} at depth {self.depth}"
            super().__init__(self.message)

    def _traverse(snailfish, depth=0, start=None, path=list()):

        if not depth:
            start = snailfish

        print(depth, snailfish, path)

        left  = snailfish[0]
        right = snailfish[1]

        # traverse left side
        if isinstance(left, list):
            _traverse(left, depth + 1, start, path + [0])
        
        # traverse right side
        if isinstance(right, list):
            _traverse(right, depth + 1, start, path + [1])

        # explode [left, right]
        if depth >= 4 and right and left:
            s = start
            print(s, 'path', path)
            for i in range(len(path)):
                s = s[path[i]]
                print(' ', s)
            raise _Action(1, depth, snailfish)

        '''
        # split left
        if left >= 10:
            raise _Action(2, depth, left)

        # split right
        if right >= 10:
            raise _Action(2, depth, right)
        '''

    action = None
    try:        
        _traverse(snailfish)
    except _Action as e:
        print(e)
        action = (e.action, e.value, e.depth)
        pass

snailfish = list()
with open('explode.txt') as f:
    for line in f:
        # yeah, eval is usually a bad thing but
        # the input is in python list format ;)
        s = eval(line.strip())
        Reduce(s)
        print()