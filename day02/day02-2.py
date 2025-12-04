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

            is_invalid = False

            for x in range(1, l//2 + 1):
                if l % x != 0:
                    continue

                pattern = s[:x]
                repeat = l // x 

                if repeat >= 2 and pattern * repeat == s:
                    is_invalid = True
                    break

            if is_invalid:
                invalid_ids.append(n)

print(f"Result: {sum(invalid_ids)}")
