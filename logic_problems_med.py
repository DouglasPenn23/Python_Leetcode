"""
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks
"""

# Final Solution
def make_bricks(small, big, goal):
    return (goal%5)<=small and (goal-(big*5))<=small


# # First unsuccessful attempt at this problem
# def make_bricks(small, big, goal):
#     # Getting the total inches of the blocks in vars
#     bigSum = (big * 5)
#     smallSum = (small * 1)

# # Section to see if either big or small blocks will go cleanly into it.

# # Big Block Section
#     # Get remainder after subtracting BigBlock inches from goal
#     goalMinusBigSum = goal - bigSum;
#     #  If the big blocks go cleanly into the goal, return True
#     if goalMinusBigSum == 0:
#         return True;

# # Small block section
#     # Get remainder after subtracting little blocks from the goal.
#     goalMinusSmallSum = goal - smallSum;
#     #   If the little blocks will go cleanly into the goal, return True
#     if goalMinusSmallSum == 0:
#         return True;

# # Check to see whether just adding the blocks together will give you the goal.
#     if smallSum + bigSum == goal:
#         return True;


# # If the blocks do not go cleanly, engage in this next part.


#     # If there's still a remainder after doing the big blocks (Aka 1 or greater)
#     if goalMinusBigSum >= 1:
#         # See if the remaining blocks can be filled with little blocks.
#         # Do this by taking the blocks needed to hit the goal & dividing it by the number of small blocks
#         goalMinusBigSumDivBySmall = goalMinusBigSum / smallSum;
#         # If the amount of blocks needed match the small ones we have, return true.
#         if goalMinusBigSumDivBySmall < 1:
#             return True;
#         # If we do not have enough small blocks return false.
#         else:
#             return False;

#     # If there's still a remainder after doing the small blocks(Aka 1 or greater)
#     if goalMinusSmallSum % 5 == 0:
#         return True;
#     else:
#         return False;
    

  

















# def make_bricks(small, big, goal):
#     # Getting the total inches of the blocks in vars
#   bigSum = (big * 5)
#   smallSum = (small * 1)

# # Section to see if either big or small blocks will go cleanly into it.

# # Big Block Section
# #   Get remainder after subtracting BigBlock inches from goal
#   goalMinusBigSum = abs(goal - bigSum);
# #   If the big blocks go cleanly into the goal, return True
#   if goalMinusBigSum == 0:
#     return True;

# # Small block section
# # Get remainder after subtracting little blocks from the goal.
#   goalMinusSmallSum = goal - smallSum;
# #   If the little blocks will go cleanly into the goal, return True
#   if goalMinusSmallSum == 0:
#     return True;

# # Check to see whether just adding the blocks together will give you the goal.
#   if smallSum + bigSum == goal:
#     return True;

# # If the blocks do not go cleanly, engage in this next part.


# # If there's still a remainder after doing the big blocks (Aka 1 or greater)
#   if goalMinusBigSum >= 1:
#     # See if the remaining blocks can be filled with little blocks.
#     # Do this by taking the blocks needed to hit the goal & dividing it by the number of small blocks
#     goalMinusBigSumDivBySmall = goalMinusBigSum / smallSum;
#     # If the amount of blocks needed match the small ones we have, return true.
#     if goalMinusBigSumDivBySmall < 1:
#       return True;
#     # If we do not have enough small blocks return false.
#     else:
#       return False;
#   else:
#     return False;