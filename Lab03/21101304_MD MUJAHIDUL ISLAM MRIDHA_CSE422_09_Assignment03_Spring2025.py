#Task1
import math
import random

def strength(x):
    return math.log2(x + 1) + (x / 10)

def utility_function(maxV, minV):
    i = random.choice([0, 1])
    return (strength(maxV) - strength(minV) + ((-1) ** i) * random.randint(1, 10)) / 10

def maximizing(depth, maxV, minV, alpha, beta, max_depth):
    if depth == max_depth:
        return utility_function(maxV, minV)

    v = -math.inf
    for i in range(2):
        v_prime = minimizing(depth + 1, maxV, minV, alpha, beta, max_depth)
        if v_prime>v:
            v=v_prime
        if v_prime>=beta:
            return v
        if v_prime>alpha:
            alpha=v_prime
    return v

def minimizing(depth, maxV, minV, alpha, beta, max_depth):
    if depth == max_depth:
        return utility_function(maxV, minV)

    v = math.inf
    for i in range(2):
        v_prime = maximizing(depth + 1, maxV, minV, alpha, beta, max_depth)
        if v_prime<v:
            v=v_prime
        if v_prime<=alpha:
            return v
        if v_prime<beta:
            beta=v_prime
    return v




def play_games(starting_player, maxV, minV):
    results = []
    for game in range(4):
        if game % 2 == 0:
            max_strength, min_strength = maxV, minV
        else:
            max_strength, min_strength = minV, maxV

        winner_value = maximizing(0,max_strength, min_strength, -math.inf, math.inf, 5)
        winner = "Magnus Carlsen" if (winner_value > 0 and starting_player == 0) or (winner_value < 0 and starting_player == 1) else "Fabiano Caruana"
        results.append((winner, winner_value))
        if starting_player==0:
            starting_player=1
        else:
            starting_player=0

    return results


starting_player = int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
maxV = int(input("Enter base strength for Carlsen: "))
minV = int(input("Enter base strength for Caruana: "))

results = play_games(starting_player, maxV, minV)
carlsen_wins = 0
caruana_wins = 0
for i in results:
    if i[0] =='Magnus Carlsen':
        carlsen_wins+=1
    else:
        caruana_wins+=1
draws = 4 - (carlsen_wins + caruana_wins)

print("\nGame Results:")
for i in range(len(results)):
      
      print(f"Game {i} Winner: {results[i][0]} (Utility value: {results[i][1]})")

print("\nOverall Results:")
print(f"Magnus Carlsen Wins: {carlsen_wins}")
print(f"Fabiano Caruana Wins: {caruana_wins}")
print(f"Draws: {draws}")
overall_winner = "Draw" if carlsen_wins == caruana_wins else ("Magnus Carlsen" if carlsen_wins > caruana_wins else "Fabiano Caruana")
print(f"Overall Winner: {overall_winner}")

#Task2
import math
import random

def strength(x):
    return math.log2(x + 1) + (x / 10)

def utility_function(maxV, minV):
    i = random.choice([0, 1])
    return (strength(maxV) - strength(minV) + ((-1) ** i) * random.randint(1, 10)) / 10

def precompute_utilities(maxV, minV):
    utilities = []
    for i in range(2 ** 6):
        utilities.append(utility_function(maxV, minV))
    return utilities

def maximizing(depth, ind, alpha, beta, util, max_depth, magic):
    if depth == max_depth:
        return util[ind]

    v = -math.inf
    for i in range(2):
        if magic==True:
            v_prime = maximizing(depth + 1, 2*ind+i, alpha, beta, util, max_depth,magic)
        else:
            v_prime = minimizing(depth + 1, 2*ind+i, alpha, beta,util, max_depth,magic)
        if v_prime>v:
            v=v_prime
        if v_prime>=beta:
            return v
        if v_prime>alpha:
            alpha=v_prime
    return v

def minimizing(depth, ind, alpha, beta, util, max_depth,magic):
    if depth == max_depth:
        return util[ind]

    v = math.inf
    for i in range(2):
        v_prime = maximizing(depth + 1,2*ind+i, alpha, beta,util, max_depth,magic)
        if v_prime<v:
            v=v_prime
        if v_prime<=alpha:
            return v
        if v_prime<beta:
            beta=v_prime
    return v


def play_game(maxV, minV, cost):
    max_depth=5
    util=precompute_utilities(maxV,minV)
    us=set(util[31:])
    print(len(us))
    minimax_without_mc = maximizing(0,0, -math.inf, math.inf, util, max_depth,False)
    minimax_with_mc = maximizing(0,0, -math.inf, math.inf, util, max_depth,True)

    mc_with_cost=minimax_with_mc-cost

    return minimax_without_mc, minimax_with_mc, mc_with_cost

starting_player = random.randint(0,1)#int(input("Enter who goes first (0 for Light, 1 for L): "))
cost = float(input("Enter the cost of using Mind Control: "))
maxV = int(input("Enter base strength for Light: "))
minV = int(input("Enter base strength for L: "))

without_magic, with_magic, with_cost=play_game(maxV,minV,cost)

players=['Light','L']

print(f"Minimax value without Mind Control: {with_magic:.2f}")
print(f"Minimax value with Mind Control: {without_magic:.2f}")
print(f"Minimax value with Mind Control after incurring the cost: {with_cost:.2f}")

if without_magic>0 and with_cost>0:
    print(players[starting_player], "should NOT use Mind Control as the position is already winning.")
elif without_magic<0 and with_cost>0:
    print(players[starting_player],'should use Mind Control.')
elif without_magic<0 and with_cost<0:
    print(players[starting_player],'should NOT use Mind Control as the position is losing either way.')
elif with_magic>0 and with_cost<0:
    print(players[starting_player], 'should NOT use Mind Control as it backfires.')
