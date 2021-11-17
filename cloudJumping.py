"""
There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.

Index the array from . The number on each cloud is its index in the list so the player must avoid the clouds at indices  and . They could follow these two paths:  or . The first path takes  jumps while the second takes . Return .

Function Description

Complete the jumpingOnClouds function in the editor below.

jumpingOnClouds has the following parameter(s):

int c[n]: an array of binary integers
Returns

int: the minimum number of jumps required
"""

#TRY ONE 34 minutes for 5/9 partial solution.
def jumpingOnClouds(c):
    # Write your code here
    #we count moves
    moveCount = 0
    #we loop and check indexes
    for index, cloud in enumerate(c):
        try:
            #is our current cloud 1? If so, skip
            print(cloud)
            if cloud == 1:
                print("Skipping bad cloud")
                pass
            #check if we can make the best possible move? (we have to double jump)
            if c[index+2] == 0 and c[index+1] == 1:
                moveCount += 1
                print("Best move in our future")
                pass
            #check if we might double count (we will count on its turn delayed)
            elif c[index+2] == 1 and c[index+1] == 0:
                print("Best move possible")
                moveCount += 1
                pass
            else:
                pass
            print("Index: " + str(index))
            print("MoveCount: " + str(moveCount))
        except IndexError:
            #if we are at the end and we look ahead, we will get index errors
            if index == (len(c)-2) and cloud == 0:
                print("Except triggered")
                moveCount += 1
            pass
    return moveCount


#wasted 1 hour, cannot figure it out after writing all cases. Solution(s)
#solution #1
#this solution checks while it is still shorter than the total length, it jumps *iterations* and always increments the jump after doing that.
#NOTE: it is using the *while loop* and incrementing the local variable. For loops are not always better.
def jumpingOnClouds(c):
    i = count_jumps = 0
    length = len(c)

    while i < length - 1:
        if i < length - 2 and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        count_jumps += 1
    return count_jumps
 
#2nd approach, same as first but easier.
#While its not at the last position, if there's a 1 in 2 slots, only move 1 forward. Else, if there's a 0 in two slots, jump. It implicitly ignores 1's because it never touches them (while loop.)
def jumpingOnClouds(c):
    i = count_jumps = 0
    length = len(c)

    while i < length - 2:
        if c[i+2] == 1:
            i += 1
        else:
            i += 2
        count_jumps += 1
    
    if i == length - 2:
        count_jumps += 1

    return count_jumps

#solution #2
#minimal solution with my comments to explain. It essentially uses the function to call it in isolation on the next two (like I tried to do with if's), and then returns passing numbers up the chain.
def jumpingOnClouds(c):
    #if the length is nothing, you don't hop
    if len(c) == 1 : return 0
    #if the length is 2, you don't hop if there's a 1, otherwise you do hop.
    if len(c) == 2: return 0 if c[1]==1 else 1
    #if the third element is 1 (001), you must jump once (1 + ...), then you call the function but on a shorter part of the slice recursively.
    if c[2]==1: 
        return 1 + jumpingOnClouds(c[1:])
    #if the third element is 0, it was 010 and you call recursively again.
    if c[2]==0:
        return 1 + jumpingOnClouds(c[2:])
