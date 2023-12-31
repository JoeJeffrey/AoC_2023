winning_numbers = []
cards = []

with open('day_4.txt','r') as F:
    for line in F.readlines():
        line = line.strip('\n').split('|')
        numbers = [int(number) for number in line[0].split(':')[1].split(' ') if number != '']
        winning_numbers.append(numbers)
        card = [int(number) for number in line[1].split(' ') if number != '']
        cards.append(card)

def count_matches(A:list,B:list) ->int:
    count = 0
    for item in A:
        if item in B:
            count+=1
    return count

total_matches = 0
for i in range(len(cards)):
    matches = count_matches(winning_numbers[i],cards[i])
    total_matches += pow(2,matches-1) if matches >0 else 0

print(total_matches)

#end of part 1

card_copies = [1 for item in cards]
for i in range(len(cards)):
    copies = card_copies[i] #number of copies of card i
    matches = count_matches(winning_numbers[i],cards[i])
    for k in range(matches):
        card_copies[i+k+1] += copies #since range is zero indexed

total_cards = sum(card_copies)
print(total_cards)
        