'''import math
import random

def strength(x):
    return math.log2(x + 1) + (x / 10)

def utility_function(maxV, minV):
    i = random.choice([0, 1])
    return (strength(maxV) - strength(minV) + ((-1) ** i) * random.randint(1, 10)) / 10

def maximizing(depth, maxV, minV, alpha, beta, max_depth, use_mind_control=False):
    if depth == max_depth:
        return utility_function(maxV, minV)

    v = -math.inf
    for i in range(2):
        if use_mind_control and depth == 0:
            # If using mind control, the MAX player can choose the best move for the MIN player
            v_prime = minimizing(depth + 1, maxV, minV, alpha, beta, max_depth, use_mind_control=True)
        else:
            v_prime = minimizing(depth + 1, maxV, minV, alpha, beta, max_depth, use_mind_control)

        if v_prime > v:
            v = v_prime
        if v_prime >= beta:
            return v
        if v_prime > alpha:
            alpha = v_prime
    return v

def minimizing(depth, maxV, minV, alpha, beta, max_depth, use_mind_control=False):
    if depth == max_depth:
        return utility_function(maxV, minV)

    v = math.inf
    for i in range(2):
        if use_mind_control and depth == 1:
            # If using mind control, the MAX player can choose the best move for the MIN player
            v_prime = maximizing(depth + 1, maxV, minV, alpha, beta, max_depth, use_mind_control=True)
        else:
            v_prime = maximizing(depth + 1, maxV, minV, alpha, beta, max_depth, use_mind_control)

        if v_prime < v:
            v = v_prime
        if v_prime <= alpha:
            return v
        if v_prime < beta:
            beta = v_prime
    return v

def play_game_with_mind_control(starting_player, maxV, minV, cost):
    # Calculate minimax value without mind control
    minimax_without_mc = maximizing(0, maxV, minV, -math.inf, math.inf, 5, use_mind_control=False)
    
    # Calculate minimax value with mind control
    minimax_with_mc = maximizing(0, maxV, minV, -math.inf, math.inf, 5, use_mind_control=True)
    
    # Calculate minimax value with mind control after incurring the cost
    minimax_with_mc_cost = minimax_with_mc - cost
    
    # Determine if the MAX player should use mind control
    if minimax_with_mc_cost > minimax_without_mc:
        should_use_mc = True
    else:
        should_use_mc = False
    
    return minimax_without_mc, minimax_with_mc, minimax_with_mc_cost, should_use_mc

# Input for Problem 02
starting_player = 0#int(input("Enter who goes first (0 for Light, 1 for L): "))
cost = 0.3#float(input("Enter the cost of using Mind Control: "))
maxV = 9#float(input("Enter base strength for Light: "))
minV = 8#float(input("Enter base strength for L: "))

# Play the game with mind control
minimax_without_mc, minimax_with_mc, minimax_with_mc_cost, should_use_mc = play_game_with_mind_control(starting_player, maxV, minV, cost)

# Output the results
print(f"Minimax value without Mind Control: {minimax_without_mc:.2f}")
print(f"Minimax value with Mind Control: {minimax_with_mc:.2f}")
print(f"Minimax value with Mind Control after incurring the cost: {minimax_with_mc_cost:.2f}")

if should_use_mc:
    print("Light should use Mind Control.")
else:
    print("Light should NOT use Mind Control.")'''

import math
import random

def strength(x):
    return math.log2(x + 1) + (x / 10)

def utility_function(maxV, minV):
    i = random.choice([0, 1])
    return (strength(maxV) - strength(minV) + ((-1) ** i) * random.randint(1, 10)) / 10

def precompute_utilities(maxV, minV, max_depth):
    # Precompute utility values for all leaf nodes
    # Since the branching factor is 2 and the depth is 5, there are 2^5 = 32 leaf nodes
    utilities = {}
    for leaf_id in range(2 ** max_depth):
        utilities[leaf_id] = utility_function(maxV, minV)
    return utilities

def maximizing(depth, maxV, minV, alpha, beta, max_depth, utilities, use_mind_control=False):
    if depth == max_depth:
        # Use precomputed utility value for the leaf node
        leaf_id = sum(2 ** i for i in range(depth))  # Unique ID for the leaf node
        return utilities[leaf_id]

    v = -math.inf
    for i in range(2):
        if use_mind_control and depth == 0:
            # If using mind control, the MAX player can choose the best move for the MIN player
            v_prime = minimizing(depth + 1, maxV, minV, alpha, beta, max_depth, utilities, use_mind_control=True)
        else:
            v_prime = minimizing(depth + 1, maxV, minV, alpha, beta, max_depth, utilities, use_mind_control)

        if v_prime > v:
            v = v_prime
        if v_prime >= beta:
            return v
        if v_prime > alpha:
            alpha = v_prime
    return v

def minimizing(depth, maxV, minV, alpha, beta, max_depth, utilities, use_mind_control=False):
    if depth == max_depth:
        # Use precomputed utility value for the leaf node
        leaf_id = sum(2 ** i for i in range(depth))  # Unique ID for the leaf node
        return utilities[leaf_id]

    v = math.inf
    for i in range(2):
        if use_mind_control and depth == 1:
            # If using mind control, the MAX player can choose the best move for the MIN player
            v_prime = maximizing(depth + 1, maxV, minV, alpha, beta, max_depth, utilities, use_mind_control=True)
        else:
            v_prime = maximizing(depth + 1, maxV, minV, alpha, beta, max_depth, utilities, use_mind_control)

        if v_prime < v:
            v = v_prime
        if v_prime <= alpha:
            return v
        if v_prime < beta:
            beta = v_prime
    return v

def play_game_with_mind_control(starting_player, maxV, minV, cost):
    # Precompute utility values for both scenarios
    max_depth = 5
    utilities_without_mc = precompute_utilities(maxV, minV, max_depth)  # Without mind control
    utilities_with_mc = precompute_utilities(maxV, minV, max_depth)     # With mind control
    
    # Calculate minimax value without mind control
    minimax_without_mc = maximizing(0, maxV, minV, -math.inf, math.inf, max_depth, utilities_without_mc, use_mind_control=False)
    
    # Calculate minimax value with mind control
    minimax_with_mc = maximizing(0, maxV, minV, -math.inf, math.inf, max_depth, utilities_with_mc, use_mind_control=True)
    
    # Calculate minimax value with mind control after incurring the cost
    minimax_with_mc_cost = minimax_with_mc - cost
    
    # Determine if the MAX player should use mind control
    if minimax_with_mc_cost > minimax_without_mc:
        should_use_mc = True
    else:
        should_use_mc = False
    
    return minimax_without_mc, minimax_with_mc, minimax_with_mc_cost, should_use_mc

# Input for Problem 02
starting_player = 0#int(input("Enter who goes first (0 for Light, 1 for L): "))
cost = 0.3#float(input("Enter the cost of using Mind Control: "))
maxV = 9#float(input("Enter base strength for Light: "))
minV = 8#float(input("Enter base strength for L: "))

# Play the game with mind control
minimax_without_mc, minimax_with_mc, minimax_with_mc_cost, should_use_mc = play_game_with_mind_control(starting_player, maxV, minV, cost)

# Output the results
print(f"Minimax value without Mind Control: {minimax_without_mc:.2f}")
print(f"Minimax value with Mind Control: {minimax_with_mc:.2f}")
print(f"Minimax value with Mind Control after incurring the cost: {minimax_with_mc_cost:.2f}")

if should_use_mc:
    print("Light should use Mind Control.")
else:
    print("Light should NOT use Mind Control.")