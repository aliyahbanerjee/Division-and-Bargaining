# This code computes expected utility of player 1 and player 2 in a simple 2-player division game from random dictatorship and equal division
# where utilities may be risk neutral or not. User must enter utility functions for players 1 and 2, as well as the total amount to be divided.
# Also checks if utiliy functions are affine, testing risk-aversion to conclude if random dictatorship and equal division expected utilities are equal
# in the given scenario.
# -----------------------------------------------------------------------------------------------------------------------------------------------------

# import necessary tools from sympy library: symbols to allow for symbolic expressions in input, lambdify to turn expressions to functions readable by Python,
# diff for second derivative in affinity checks later, and simplify for simplifying algebraic expressions. parse_expr for converting string input to symbolic expression.

from sympy import symbols, lambdify, diff, simplify
from sympy.parsing.sympy_parser import parse_expr

# take inputs for utility functions for players 1 and 2, in the form of expressions using standard Python operators. Only allow for functions well-defined at 0, since random
# dictatorship is subject to constraint that player other than dictator gets 0. 
uf_player1 = input("Enter utility function of player 1 as a function of x, their allocation. Function must be well-defined at 0: ")
uf_player2 = input("Enter utility function of player 2 as a function of x, their allocation. Function must be well-defined at 0: ")

# take input for total amount to be divided and convert to float. Assume the good is divisible, with the allocation space for each player being continuous. 
amount = float(input("Enter total amount to be divided: "))

# identify x as symbolic variable
x = symbols('x')

# convert input strings into symbolic expressions
expr1 = parse_expr(uf_player1)
expr2 = parse_expr(uf_player2)

# convert symbolic expressions into callable numeric functions. 
p1utility = lambdify(x, expr1)
p2utility = lambdify(x, expr2)

# define random dictatorship expected utility for players 1 and 2. Random dictatorship is subject to constraint that other player gets 0 i.e. dictator gets entire amount.
# random dictatorship is defined as equal probability between player 1 or 2 being the dictator. 
rd_eu_1 = (p1utility(amount) * 0.5) + (p1utility(0) * 0.5)
rd_eu_2 = (p2utility(amount) * 0.5) + (p2utility(0) * 0.5)

# define equal division expected utility for players 1 and 2. Each player gets exactly half the amount. 
ed_eu_1 = p1utility((amount/2))
ed_eu_2 = p2utility((amount/2))

# check linear form of both utility functions using second derivative is equal to 0. Linearity represents risk neutrality, in which random dictatorship and equal division expected
# utility of a player is equal. 
linearity_check = (
    simplify(diff(expr1, x, x)) == 0 and
    simplify(diff(expr2, x, x)) == 0)

# if both players' utility functions are linear, state that and return expected utilities of random dictatorship for each player. Equal division expected utilities are the same. 
if linearity_check:
    print(f"Players are risk neutral. Expected utility for player 1 is {rd_eu_1}. "
          f"Expected utility for player 2 is {rd_eu_2}. "
          f"Expected utility for each player is the same from random dictatorship or equal division.")

# if atleast one player is not linear in their utility function, state that and return both players' expected utilities from random dictatorship and equal division. 
else:
    print(f"One or more players are not risk neutral. "
          f"Expected utility from random dictatorship is {rd_eu_1} for player 1 and {rd_eu_2} for player 2. "
          f"Expected utility from equal division is {ed_eu_1} for player 1 and {ed_eu_2} for player 2.")
