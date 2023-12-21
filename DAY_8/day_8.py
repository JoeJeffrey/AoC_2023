Graph = {}

with open('day_8.txt','r') as F:
    instructions = F.readline().strip('\n')
    F.readline()
    for line in F:
        line = line.split(' ')
        Graph[line[0]] = [line[2][1:-1], line[3][:-2]]

count = 0
current = 'AAA'
ci = 0 #current instruction
length = len(instructions)
while current != 'ZZZ':
    current = Graph[current][instructions[ci] == 'R'] #goes left if L goes right if R
    count +=1
    ci = count % length

print(count)

##end of part 1
#in part two you take all of the nodes ending with A
#and you run the algorithm untill all the threads land on a
#node ending in Z

#The graph always cycles for these 6 nodes (by inspection)
#so just need the lcm of the 6 cycle lengths

def get_cycle_length(node):
    count = 0
    ci = 0
    global length,instructions
    while node[-1] !='Z':
        node = Graph[node][instructions[ci] == 'R']
        count += 1
        ci = count % length
    return count

Cycles = [get_cycle_length(node) for node in Graph if node[-1] == 'A']

import math
LCM = 1
for item in Cycles:
    LCM = math.lcm(LCM,item)

print(LCM)



    