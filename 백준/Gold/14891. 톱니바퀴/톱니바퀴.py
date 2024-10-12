# https://www.acmicpc.net/problem/14891


class Gear:
    def __init__(self, status):
        self._status = status

    def status(self):
        return self._status

    def rotate(self, rdir):
        if rdir == 1:
            self._status = self._status[-1] + self._status[:-1]
        else:
            self._status = self._status[1:] + self._status[0]

    def left(self):
        return self._status[-2]

    def right(self):
        return self._status[2]


G = [Gear(input()) for _ in range(4)]


def rotate(n, dir, rdir):
    if dir >= 0 and n != 3 and G[n].right() != G[n + 1].left():
        rotate(n + 1, 1, -rdir)
    if dir <= 0 and n != 0 and G[n].left() != G[n - 1].right():
        rotate(n - 1, -1, -rdir)
    G[n].rotate(rdir)


for _ in range(int(input())):
    n, rdir = map(int, input().split())
    rotate(n - 1, 0, rdir)

print(sum([2 ** (i) for i in range(4) if G[i].status()[0] == "1"]))