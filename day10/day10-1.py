#!/usr/bin/env python3
class Clock:
    def __init__(self):
        self.cycle = 0
        self.signal_strength = 0

    def inc(self, x):
        self.cycle += 1
        if self.cycle in range(20, 221, 40):
            self.signal_strength += x * self.cycle


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

result = clock.signal_strength

print(f"Result: {result}")
