#!/usr/bin/env python3
class Clock:
    def __init__(self):
        self.cycle = 0
        self.signal_strength = 0
        self.display = ["░" for _ in range(240)]

    def inc(self, pos):
        if self.cycle % 40 in [pos - 1, pos, pos + 1]:
            self.display[self.cycle] = "█"
        self.cycle += 1


with open("input.txt") as f:
    data = f.read().splitlines()

x = 1
clock = Clock()
for line in data:
    match line.split():
        case ["noop"]:
            clock.inc(x)
        case ["addx", number]:
            clock.inc(x)
            clock.inc(x)
            x += int(number)

result = ""
for row in range(6):
    start = row * 40
    result += "".join(clock.display[start : start + 40]) + "\n"

print(f"Result: \n{result}")
