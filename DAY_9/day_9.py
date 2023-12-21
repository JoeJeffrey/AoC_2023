
sequence = [i*3 for i in range(6)]
sequence = [1,4,9,16]

def decompose(sequence):
    parts = [sequence]
    working = sequence 
    while not all(item == 0 for item in working):
        working = [working[i] - working[i-1] for i in range(1,len(working))]
        parts.append(working)
    parts.reverse()
    return parts

def generate_new(parts):
    parts[0].append(0)
    for i in range(1,len(parts)):
        parts[i].append(parts[i][-1]+parts[i-1][-1])
    return parts[-1]

def get_extrapolated_value(sequence):
    return generate_new(decompose(sequence))[-1]

Sequences = []
with open('day_9.txt','r') as F:
    for line in F:
        line = line.strip('\n').split(' ')
        Sequences.append([int(x) for x in line])

SUM = sum(get_extrapolated_value(sequence) for sequence in Sequences)
#SUM = 1834108701
##END OF PART 1

#for part two instead of extrapolating forwards you extrapolate backwards
#for this you can simply reverse the input list xx
SUM = sum(get_extrapolated_value(sequence[::-1]) for sequence in Sequences)
#SUM = 993