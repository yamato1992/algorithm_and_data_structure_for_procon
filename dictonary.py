class Dictonary:

    def __init__(self):
        self.d = set()

    def insert(self, s: str):
        if s not in self.d:
            self.d.add(s)

    def find(self, s: str):
        if s in self.d:
            print('yes')
        else:
            print('no')

d = Dictonary()
n = int(input())

for _ in range(n):
    cmd, s = input().split()
    if cmd == 'insert':
        d.insert(s)
    elif cmd == 'find':
        d.find(s)
