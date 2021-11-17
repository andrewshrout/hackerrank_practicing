"""An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Function Description

Complete the countingValleys function in the editor below.

countingValleys has the following parameter(s):

int steps: the number of steps on the hike
string path: a string describing the path
Returns

int: the number of valleys traversed
Input Format

The first line contains an integer , the number of steps in the hike.
The second line contains a single string , of  characters that describe the path.
"""


#First attempt took 40 minutes. Didn't understand question parameters
#NOTE: Read questions better
#Tried it out on paper
#second attempt -> 4 minutes 9 seconds


def countingValleys(steps, path):
    #Our current height
    seaLevel = 0
    #Valleys crossed
    valleys = 0
    #Track our movements
    for x in path[:steps]:
        #if it's a D, we go down. Else, we go up.
        print(x)
        if x == 'D':
            seaLevel -= 1
        else:
            seaLevel += 1
            #A valley only "triggers" if we finally left it. If we are above it, it doesn't matter.
            if seaLevel == 0:
                valleys += 1
    return valleys

#Note: not nesting my if would probably be a faster algo. example below

def countingValleys(n, steps):
    seaLevel = valley = 0

    for step in steps:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1
        
        if step == 'U' and seaLevel == 0:
            valley += 1
    
    return valley
