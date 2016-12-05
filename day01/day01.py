input = 'L1, L5, R1, R3, L4, L5, R5, R1, L2, L2, L3, R4, L2, R3, R1, L2, R5, R3, L4, R4, L3, R3, R3, L2, R1, L3, R2, L1, R4, L2, R4, L4, R5, L3, R1, R1, L1, L3, L2, R1, R3, R2, L1, R4, L4, R2, L189, L4, R5, R3, L1, R47, R4, R1, R3, L3, L3, L2, R70, L1, R4, R185, R5, L4, L5, R4, L1, L4, R5, L3, R2, R3, L5, L3, R5, L1, R5, L4, R1, R2, L2, L5, L2, R4, L3, R5, R1, L5, L4, L3, R4, L3, L4, L1, L5, L5, R5, L5, L2, L1, L2, L4, L1, L2, R3, R1, R1, L2, L5, R2, L3, L5, L4, L2, L1, L2, R3, L1, L4, R3, R3, L2, R5, L1, L3, L3, L3, L5, R5, R1, R2, L3, L2, R4, R1, R1, R3, R4, R3, L3, R3, L5, R2, L2, R4, R5, L4, L3, L1, L5, L1, R1, R2, L1, R3, R4, R5, R2, R3, L2, L1, L5'

dirs = input.split(', ')

def get_next_dirs(cur_xdir, cur_ydir, turn_dir):
    if turn_dir == 'L':
        if cur_xdir != 0:
            return 0, cur_xdir
        return -cur_ydir, 0
    elif turn_dir == 'R':
        if cur_xdir != 0:
            return 0, -cur_xdir
        return cur_ydir, 0
    else:
        raise RuntimeError('Unknown turn direction')

assert (get_next_dirs(0, 1, 'L') == (-1, 0))
assert (get_next_dirs(1, 0, 'L') == (0, 1))
assert (get_next_dirs(-1, 0, 'L') == (0, -1))
assert (get_next_dirs(0, -1, 'L') == (1, 0))


assert (get_next_dirs(0, 1, 'R') == (1, 0))
assert (get_next_dirs(1, 0, 'R') == (0, -1))
assert (get_next_dirs(-1, 0, 'R') == (0, 1))
assert (get_next_dirs(0, -1, 'R') == (-1, 0))

dx = 0
dy = 0
xdir = 0
ydir = 1
locations = set()
loc_found = False
duplicate_location = None

for d in dirs:
    xdir, ydir = get_next_dirs(xdir, ydir, d[0])
    steps = int(d[1:])

    for s in range(steps):
        loc = dx, dy

        if loc not in locations:
            locations.add(loc)
        else:
            if not loc_found:
                duplicate_location = loc
                loc_found = True

        dx += xdir
        dy += ydir

print('Part 1: dx={dx}, dy={dy}, dist={d}'.format(dx=dx, dy=dy, d=abs(dx) + abs(dy)))
print('Part 2: duplicated location={loc}'.format(loc=duplicate_location))





