# Dice game, points are as follows
# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point
def score(dice):  #calculates points from dice
    total = 0
    dice.sort()
    print(dice)
    if dice.count(1) >= 3: 
        total += 1000
        del dice[:3]
    for x, i in enumerate(dice):
        print(x,i)
        if dice.count(i) >= 3:
            total += (i*100)
            del dice[x:x+3]
    for i in dice:
        if i == 1:
            total += 100
        if i == 5:
            total += 50
    return total
