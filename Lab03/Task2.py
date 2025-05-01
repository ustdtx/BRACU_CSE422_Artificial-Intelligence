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


