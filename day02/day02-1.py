#!/usr/bin/env python3
with open('input.txt', 'r') as infile:
    data = [x.split(',') for x in infile.read().strip().replace('\n', '').split('\n\n')]


invalid_ids = []
for i in range(len(data)):
    for item in data[i]:
        start, end = map(int, item.split('-'))
        extended = (list(range(start, end + 1)))
        for n in extended:
            s = str(n)
            l = len(s)

            if l % 2 != 0:
                continue

            half = l // 2
            if s[:half] == s[half:]:
                invalid_ids.append(n)


print(f"Result: {sum(invalid_ids)}")
