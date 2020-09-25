# 232. Implement Queue using Stacks
# Easy
# Add to List

# Share
# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Example:

# MyQueue queue = new MyQueue();

# queue.push(1);
# queue.push(2);  
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
# Notes:

# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

class MyQueue(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1=[]
        self.s2=[]

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.s1.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.s1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.s1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self):
        return not self.s1 and not self.s2

# Search in Rotated Sorted Array
# Medium
# Add to List

# Share
# You are given an integer array nums sorted in ascending order, and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# If target is found in the array return its index, otherwise, return -1.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = nums.index(target) if target in nums else -1
        return i

# Find the Duplicate Number
# Medium

# 5594

# 634

# Add to List

# Share
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one duplicate number in nums, return this duplicate number.

# Follow-ups:

# How can we prove that at least one duplicate number must exist in nums? 
# Can you solve the problem without modifying the array nums?
# Can you solve the problem using only constant, O(1) extra space?
# Can you solve the problem with runtime complexity less than O(n2)?
 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [1,1]
# Output: 1
# Example 4:

# Input: nums = [1,1,2]
# Output: 1
 

# Constraints:

# 2 <= n <= 3 * 104
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if i in counter:
                return i
            counter[i] = 0

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = DefaultDict(int)
        for num in nums:
            dic[num] += 1
            if dic[num] > 1: return num