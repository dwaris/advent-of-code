#!/usr/bin/env python3
class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0

    @property
    def pos(self):
        return self.x, self.y


class Head(Knot):
    def step(self, heading):
        match heading:
            case "U":
                self.y += 1
            case "D":
                self.y -= 1
            case "L":
                self.x -= 1
            case "R":
                self.x += 1
            case _:
                raise ValueError(f"Unknown heading: {heading}")


class Tail(Knot):
    def __init__(self):
        super().__init__()
        self.path = set()

    def follow(self, pos):
        x, y = pos
        d_x = x - self.x
        d_y = y - self.y
        if abs(d_x) == 2 and not d_y:
            self.x += 1 if d_x > 0 else -1
        elif abs(d_y) == 2 and not d_x:
            self.y += 1 if d_y > 0 else -1
        elif (abs(d_y) == 2 and abs(d_x) in (1, 2)) or (
            abs(d_x) == 2 and abs(d_y) in (1, 2)
        ):
            self.x += 1 if d_x > 0 else -1
            self.y += 1 if d_y > 0 else -1
        self.path.add((self.x, self.y))


with open("input.txt", "r") as f:
    data = f.read().splitlines()

head = Head()
tails = [Tail() for _ in range(9)]

for line in data:
    heading, steps = line.split()
    for _ in range(int(steps)):
        head.step(heading)
        tails[0].follow(head.pos)
        for i in range(1, 9):
            tails[i].follow(tails[i - 1].pos)

result = len(tails[8].path)

print(f"Result: {result}")
