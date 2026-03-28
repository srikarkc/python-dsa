from collections import defaultdict

class Solution:
    def __init__(self):
        self.points = defaultdict(list)

    def add(self, point):
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point):
        x, y = point
        res = 0

        for (px, py), freq in self.points.items():
            if px != x or py == y:
                continue

            side = py - y

            res += (
                freq
                * self.points.get((x + side, y), 0)
                * self.points.get((x + side, py), 0)
            )

            res += (
                freq
                * self.points.get((x - side, y), 0)
                * self.points.get((x - side, py), 0)
            )

        return res