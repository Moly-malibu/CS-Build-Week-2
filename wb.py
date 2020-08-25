def addTwoDigits(n):
    d1 = n%10
    d2 = (n-d1)/10
    return d1+d2


# AdjacentElementsProduct
# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
# Example
# For inputArray = [3, 6, -2, -5, 7, 3], the output should be adjacentElementsProduct(inputArray) = 21. 7 and 3 produce the largest product.
# Input/Output
# [time limit] 4000ms (py)
# [input] array.integer inputArray: An array of integers containing at least two elements. Guaranteed constraints: 2 ≤ inputArray.length ≤ 10, -1000 ≤ inputArray[i] ≤ 1000.
# [output] integer: The largest product of adjacent elements.

def adjacentElementsProduct(inputArray):
    ll = [x*y for (x,y) in zip(inputArray[:-1], inputArray[1:])]
    return max(ll)

#ShapeArea
# Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n. A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.
# Example
# For n = 2, the output should be shapeArea(n) = 5; For n = 3, the output should be shapeArea(n) = 13.
# Input/Output
# [time limit] 4000ms (py)
# [input] integer n: Guaranteed constraints: 1 ≤ n < 104.
# [output] integer: The area of the n-interesting polygon.

def shapeArea(n):
    area = 1
    while n>1:
        area += (n-1)*4
        n -=1
    return area

#MakeArrayConsecutive2
# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
# Example
# For statues = [6, 2, 3, 8], the output should be makeArrayConsecutive2(statues) = 3. Ratiorg needs statues of sizes 4, 5 and 7.
# Input/Output
# [time limit] 4000ms (py)
# [input] array.integer statues: An array of distinct non-negative integers. Guaranteed constraints:1 ≤ statues.length ≤ 10, 0 ≤ statues[i] ≤ 20.
# [output] integer: The minimal number of statues that need to be added to existing statues such that it contains every integer size from an interval [L, R] (for some L, R) and no other sizes.

def makeArrayConsecutive2(statues):
    statues.sort()
    if len(statues) > 1:
        diff_statues = [y-x for x, y in zip(statues[:-1], statues[1:])]
        return sum(i-1 for i in diff_statues)
    else:
        return 0

#AlmostIncreasingSequence:
# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
# Example
# For sequence = [1, 3, 2, 1], the output should be almostIncreasingSequence(sequence) = false; There is no one element in this array that can be removed in order to get a strictly increasing sequence. For sequence = [1, 3, 2], the output should be almostIncreasingSequence(sequence) = true.
# You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
# Input/Output
# [time limit] 4000ms (py)
# [input] array.integer sequence: Guaranteed constraints: 2 ≤ sequence.length ≤ 105, -105 ≤ sequence[i] ≤ 105.
# [output] boolean: Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.

def almostIncreasingSequence(sequence):
    dff_seq = [x>=y for x, y in zip(sequence[:-1], sequence[1:])]
    if sum(dff_seq) >=2:
        return False
    elif sum(dff_seq) == 0:
        return True
    else:
        ind = dff_seq.index(True)
        t_seq = list(sequence);
        t_seq.pop(ind+1)
        dff_seq1 = [x>=y for x, y in zip(t_seq[:-1], t_seq[1:])]
        t_seq = list(sequence);
        t_seq.pop(ind)
        dff_seq2 = [x>=y for x, y in zip(t_seq[:-1], t_seq[1:])]
        return sum(dff_seq1)<1 or sum(dff_seq2)<1

#MatrixElementsSum
# After becoming famous, CodeBots decided to move to a new building and live together. The building is represented by a rectangular matrix of rooms, each cell containing an integer - the price of the room. Some rooms are free (their cost is 0), but that's probably because they are haunted, so all the bots are afraid of them. That is why any room that is free or is located anywhere below a free room in the same column is not considered suitable for the bots. Help the bots calculate the total price of all the rooms that are suitable for them.
# Example
# For matrix = [[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]], the output should be matrixElementsSum(matrix) = 9.
# Heres the rooms matrix with unsuitable rooms marked with 'x': [[x, 1, 1, 2], [x, 5, x, x], [x, x, x, x]] Thus, the answer is 1 + 5 + 1 + 2 = 9.
# Input/Output
# [time limit] 4000ms (py)
# [input] array.array.integer matrix: 2-dimensional array of integers representing a rectangular matrix of the building. Guaranteed constraints: 1 ≤ matrix.length ≤ 5, 1 ≤ matrix[i].length ≤ 5, 0 ≤ matrix[i][j] ≤ 10.
# [output] integer

def matrixElementsSum(matrix):
    costSum = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if x>0:
                if matrix[x-1][y] == 0:
                    matrix[x][y] = 0
            costSum += matrix[x][y]
    return costSum

# allLongestStrings
# Given an array of strings, return another array containing all of its longest strings.
# Example
# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
# Input/Output
# [time limit] 4000ms (py)
# [input] array.string inputArray: A non-empty array. Guaranteed constraints: 1 ≤ inputArray.length ≤ 10, 1 ≤ inputArray[i].length ≤ 10.
# [output] array.string: Array of the longest strings, stored in the same order as in the inputArray.

def allLongestStrings(inputArray):
    lenString = [len(i_string) for i_string in inputArray]
    max_len = max(lenString)
    ind = [i for i in range(len(lenString)) if lenString[i]==max_len]
    return [inputArray[nind] for nind in ind]

# commonCharacterCount
# Given two strings, find the number of common characters between them.
# Example
# For s1 = "aabcc" and s2 = "adcaa", the output should be commonCharacterCount(s1, s2) = 3. Strings have 3 common characters - 2 "a"s and 1 "c".
# Input/Output
# [time limit] 4000ms (py)
# [input] string s1: A string consisting of lowercase latin letters a-z. Guaranteed constraints: 3 ≤ s1.length ≤ 15.
# [input] string s2： A string consisting of lowercase latin letters a-z. Guaranteed constraints: 4 ≤ s2.length ≤ 15.
# [output] integer
def commonCharacterCount(s1, s2):
    n_common = 0
    for n_s1 in s1:
        if n_s1 in s2:
            n_common += 1
            s2 = s2.replace(n_s1, "", 1)
    return n_common

# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
# Example
# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
# Input/Output
# [time limit] 4000ms (py) [input] array.integer a
# If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.
# Guaranteed constraints: 5 ≤ a.length ≤ 15, -1 ≤ a[i] ≤ 200.
# [output] array.integer
# Sorted array a with all the trees untouched.

def sortByHeight(a):
    tree_index = [i for i in range(len(a)) if a[i] !=-1]
    tree_A = [i for i in a if i !=-1]
    tree_A.sort()
    for n_index, n_A in zip(tree_index, tree_A):
        a[n_index] = n_A
    return aa

# You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets. It is guaranteed that the parentheses in s form a regular bracket sequence. Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair. The results string should not contain any parentheses.
# Example
# For string s = "a(bc)de", the output should be reverseParentheses(s) = "acbde".
# Input/Output
# [time limit] 4000ms (py) [input] string s
# A string consisting of English letters, punctuation marks, whitespace characters and brackets. It is guaranteed that parentheses form a regular bracket sequence.
# Constraints: 5 ≤ s.length ≤ 55.
# [output] string

def reverseInParentheses(inputString):
    while '(' in inputString:
        last = [i for i in range(len(inputString)) if inputString[i] == ')']
        last = min(last)
        first = [i for i in range(last) if inputString[i] == '(']
        first = max(first)
        inputString = inputString[:first] + inputString[last - 1:first:-1] + inputString[last+1:]
    return inputStrings
