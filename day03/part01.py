with open('part01.txt') as f:
    input_data = f.read().splitlines()

input_data = [[int(i) for i in r.split("  ") if i != ''] for r in input_data]


def is_valid(sides):
    sides = sorted(sides)
    if sides[0] + sides[1] > sides[2]:
        return True

possible_triangles = 0
for s in input_data:
    if is_valid(s):
        possible_triangles += 1

print("Part 1:", possible_triangles)    # 862

possible_triangles = 0
for r in range(0, len(input_data), 3):
    for c in range(0, 3):
        if is_valid([input_data[r][c], input_data[r + 1][c], input_data[r + 2][c]]):
            possible_triangles += 1

print("Part 2:", possible_triangles)    # 1577