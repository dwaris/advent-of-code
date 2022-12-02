with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

mapped_values = { 'A': 1,
                  'B': 2,
                  'C': 3,
                  'X': 1,
                  'Y': 2,
                  'Z': 3 }  
result = 0

for game in lines:
    p1, p2 = game.split(' ')

    if mapped_values[p2] == 2:
      result += mapped_values[p1] + 3
    
    elif mapped_values[p2] == 3:
      result += mapped_values[p1] % 3 + 7
    
    else:
      result += (mapped_values[p1] - 2) % 3 + 1

print(f"Result: {result}")
