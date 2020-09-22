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

# Given a divisor and a bound, find the largest integer N such that:
# N is divisible by divisor.
# N is less than or equal to bound.
# N is greater than 0.
# It is guaranteed that such a number exists.
# Example
# For divisor = 3 and bound = 10, the output should be
# maxMultiple(divisor, bound) = 9.

# The largest integer divisible by 3 and not larger than 10 is 9.
def maxMultiple(divisor, bound):
    for num in range(bound, 1, -1):
        if num % divisor == 0:
            return num
    return 0 



# Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).
# Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.
# Example
# For n = 10 and firstNumber = 2, the output should be
# circleOfNumbers(n, firstNumber) = 7.

def circleOfNumbers(n, firstNumber):
    return (firstNumber + (n//2))%n

# One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins counting the length of your ride, in minutes. Off you go to explore the neighborhood.
# When you finally decide to head back, you realize there's a chance the bridges on your route home are up, leaving you stranded! Unfortunately, you don't have your watch on you and don't know what time it is. All you know thanks to the bike's timer is that n minutes have passed since 00:00.
# Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.
# Example
# For n = 240, the output should be
# lateRide(n) = 4.
# Since 240 minutes have passed, the current time is 04:00. The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.
# For n = 808, the output should be
# lateRide(n) = 14.
# 808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.

def lateRide(n):
    hours = n // 60
    minutes = n % 60
    return (hours // 10) + (hours % 10) + (minutes // 10) + (minutes % 10)

# Some phone usage rate may be described as follows:
# first minute of a call costs min1 cents,
# each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
# each minute after 10th costs min11 cents.
# You have s cents on your account before the call. What is the duration of the longest call (in minutes rounded down to the nearest integer) you can have?
# Example
# For min1 = 3, min2_10 = 1, min11 = 2, and s = 20, the output should be
# phoneCall(min1, min2_10, min11, s) = 14.
# Here's why:
# the first minute costs 3 cents, which leaves you with 20 - 3 = 17 cents;
# the total cost of minutes 2 through 10 is 1 * 9 = 9, so you can talk 9 more minutes and still have 17 - 9 = 8 cents;
# each next minute costs 2 cents, which means that you can talk 8 / 2 = 4 more minutes.
# Thus, the longest call you can make is 1 + 9 + 4 = 14 minutes long.

def phoneCall(min1, min2_10, min11, s):
    if s<min1:
        return 0
    if s == min1:
        return 1
    if s <= min1 + (min2_10*9):
        s -= min1
        return (s//min2_10) +1
    s -= min2_10 * 9
    s -= min1
    return (s//min11) + 10
