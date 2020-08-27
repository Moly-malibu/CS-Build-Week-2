# Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

# You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

# Example

# For a = [50, 60, 60, 45, 70], the output should be
# alternatingSums(a) = [180, 105].

# Input/Output

# [execution time limit] 4 seconds (py)

# [input] array.integer a

# Guaranteed constraints:
# 1 ≤ a.length ≤ 105,
# 45 ≤ a[i] ≤ 100.

def alternatingSums(a):
    team1 = sum(a[0::2])
    team2 = sum(a[1::2])
    return[team1, team2]

# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Example

# For

# picture = ["abc",
#            "ded"]
# the output should be

# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]

def addBorder(picture):
    picture = ['*' + string +'*' for string in picture]
    picture = [('*' * len(picture[0]))] + picture + ['*' * len(picture[0])]
    return picture

# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
# Given two arrays a and b, check whether they are similar.

def areSimilar(a, b):
    simm = [i for i in range(len(a)) if a [i] != b[i]]
    if len(simm) == 2:
        b[simm[0]], b[simm[1]] = b[simm[1]], b[simm[0]]
    return a==b

# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
# Example
# For inputArray = [1, 1, 1], the output should be
# arrayChange(inputArray) = 3.

def arrayChange(inputArray):
    count = 0
    for i in range(1, len(inputArray)):
        if inputArray[i-1] >= inputArray[i]:
            different = inputArray[i-1] - inputArray[i]
            inputArray[i] += different +1
            count += different +1
    return count

# Given a string, find out if its characters can be rearranged to form a palindrome.
# Example
# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.
# We can rearrange "aabb" to make "abba", which is a palindrome.

def palindromeRearranging(inputString):
    inputL = sorted(inputString)
    FMiddle = False
    while len(inputL) >1:
        if inputL[0] == inputL[1]:
            del inputL[1]
        elif not FMiddle:
            FMiddle = True
        else:
            return False
        del inputL[0]
    return len(inputL) == 0 or not FMiddle

# Call two arms equally strong if the heaviest weights they each are able to lift are equal.
# Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.
# Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
# Example
# For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
# For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
# For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    equally = yourLeft == friendsLeft and yourRight == friendsRight
    different = yourLeft == friendsRight and yourRight == friendsLeft
    return equally or different

# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
# Example
# For inputArray = [2, 4, 1, 0], the output should be
# arrayMaximalAdjacentDifference(inputArray) = 3.

def arrayMaximalAdjacentDifference(inputArray):
    abs_diff = []
    for i in range(len(inputArray) - 1):
        abs_diff.append(abs(inputArray[i]-inputArray[i+1]))
    return max(abs_diff)

#You are given a two-digit integer n. Return the sum of its digits.

def addTwoDigits(n):
    return(n//10) + (n%10)

#Given an integer n, return the largest number that contains exactly n digits.
# Example
# For n = 2, the output should be
# largestNumber(n) = 99.
def largestNumber(n):
    return int('9' * n)

# n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly the same amount of candy as any other child. Determine how many pieces of candy will be eaten by all the children together. Individual pieces of candy cannot be split.
# Example
# For n = 3 and m = 10, the output should be
# candies(n, m) = 9.
# Each child will eat 3 pieces. So the answer is 9.

def candies(n, m):
    return(m/n)*n

# Your friend advised you to see a new performance in the most popular theater in the city. He knows a lot about art and his advice is usually good, but not this time: the performance turned out to be awfully dull. It's so bad you want to sneak out, which is quite simple, especially since the exit is located right behind your row to the left. All you need to do is climb over your seat and make your way to the exit.
# The main problem is your shyness: you're afraid that you'll end up blocking the view (even if only for a couple of seconds) of all the people who sit behind you and in your column or the columns to your left. To gain some courage, you decide to calculate the number of such people and see if you can possibly make it to the exit without disturbing too many people.
# Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column you're sitting in, return the number of people who sit strictly behind you and in your column or to the left, assuming all seats are occupied.
# Example
# For nCols = 16, nRows = 11, col = 5, and row = 3, the output should be
# seatsInTheater(nCols, nRows, col, row) = 96.

def seatsInTheater(nCols, nRows, col, row):
    return (nCols-col+1)*(nRows-row)