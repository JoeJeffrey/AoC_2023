grid = []

with open('day11.txt','r') as F:
    for line in F:
        line = line.strip('\n')
        grid.append([x for x in line])

expand_rows = [i for i in range(len(grid)) if all([x=='.' for x in grid[i]])]
expand_cols = [i for i in range(len(grid[0])) if all(x=='.' for x in [grid[j][i] for j in range(len(grid))]  )]

# new_grid = []
# for row in range(len(grid)):
#     new_row = []
#     for column in range(len(grid[0])): #length of a row
#         if column in expand_cols:
#             new_row.append(grid[row][column])
#         new_row.append(grid[row][column])
#     if row in expand_rows:
#         new_grid.append(new_row)
#     new_grid.append(new_row)

# galaxy_locations = [(row,column) for row in range(len(new_grid)) for column in range(len(new_grid[0])) if new_grid[row][column] == '#']

# distance = lambda a,b: abs(a[0]-b[0])+abs(a[1]-b[1]) #-1 because you dont count where you start from

# galaxies = len(galaxy_locations)
# galaxy_pairs = [(galaxy_locations[a],galaxy_locations[b]) for a in range(1,galaxies) for b in range(a)]
# distances = [distance(p[0],p[1]) for p in galaxy_pairs]

# print(sum(distances))

## part 2
# will discard the new grid since this would become inpractical
# part 1 uses expansion factor of 2 part 2 uses expansion factor 1_000_000
expansion_factor = 1_000_000

galaxy_locations = [(row,column) for row in range(len(grid)) for column in range(len(grid[0])) if grid[row][column] == '#']
row_expansions = lambda a,b : len([x for x in expand_rows if a<x<b]) #can be strict since if there is a galaxy obviously there wont be an expansion there
col_expansions = lambda a,b : len([x for x in expand_cols if a<x<b])

galaxies = len(galaxy_locations)
galaxy_pairs = [(galaxy_locations[a],galaxy_locations[b]) for a in range(1,galaxies) for b in range(a)]

offset = lambda a,b : (expansion_factor-1)*(row_expansions(min(a[0],b[0]),max(a[0],b[0]))+col_expansions(min(a[1],b[1]),max(a[1],b[1])))
distance = lambda a,b : abs(a[0]-b[0])+abs(a[1]-b[1]) + offset(a,b)

distances = [distance(p[0],p[1]) for p in galaxy_pairs]
print(sum(distances))
