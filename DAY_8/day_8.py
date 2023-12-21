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
    current = Graph[current][instructions[ci] == 'R']
    count +=1
    ci = count % length

print(count)