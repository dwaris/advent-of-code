import re

def read():
    with open("day14/input.txt") as f:
        m = f.read().split("\n\n")
    return m[0], {k:v for k, v in re.findall("(\S+) -> (\S+)", m[1])}

def poly(steps):
    start, rules = read()
    state = {k:0 for k in rules.keys()}
    score = {k:0 for k in set(rules.values())}

    for i in range(len(start) - 1):
        state[start[i:i+2]] += 1
    for i in range(len(start)):
        score[start[i]] += 1

    for _ in range(steps):
        new_state = {k:0 for k in rules.keys()}
        for k, v in state.items():
            x = rules[k]
            new_state[k[0] + x] += v
            new_state[x + k[1]] += v
            score[x] += v
        state = new_state

    print(max(score.values()) - min(score.values()))

poly(10)
poly(40)