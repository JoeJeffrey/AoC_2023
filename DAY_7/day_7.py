
def get_groups_1(cards): #returns group structure
    cards = list(cards)
    cards = sorted(cards)
    groups = [len([card for x in cards if x == card]) for card in set(cards)]
    groups = sorted(groups,reverse= True)
    return groups

wagers = {}
with open('day_7.txt','r') as F:
    for line in F:
        line = line.strip('\n').split(' ')
        wagers[line[0]] = int(line[1])

SYMBOLS = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
encode = lambda A: [SYMBOLS.index(x) for x in A]
grouping = lambda A: get_groups_1(A)

def evaluate_encoding(encode,grouping):
    groups = [(grouping(cards) + encode(cards),cards) for cards in wagers]
    
    groups = sorted(groups,key = lambda A: A[0])
    
    SUM = sum(wagers[groups[i][1]]*(i+1) for i in range(len(groups)))
    #x by i+1 since groups is zero indexed
    return SUM

print(evaluate_encoding(encode,grouping))
#SUM = 250120186

##END OF PART ONE
#For part 2 J plays the role of Joker, it turns into a wildcard

def get_groups_2(cards):
    Jokers = len([x for x in cards if x=='J'])
    remaining = [x for x in cards if x!='J']
    group = get_groups_1(remaining)
    if group == []:
        group = [0]
    group[0]+=Jokers
    return group

SYMBOLS = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
encode = lambda A: [SYMBOLS.index(x) for x in A]
grouping = lambda A: get_groups_2(A)

print(evaluate_encoding(encode, grouping))
#SUM = 250665248