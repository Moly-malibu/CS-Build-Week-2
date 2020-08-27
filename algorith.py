
class node:
        def __init__(self, data = None, next = None):
                self.data = data
                self.next = next

class linked_list:
        def __init__(self):
                self.head = None

        # function to add a node at front
        def add_at_front(self, data):
                self.head = node(data=data, next=self.head) 

        # function to check whether the list is empty
        def is_empty(self):
                return self.head == None

        # function to add node at the end
        def add_at_end(self, data):
                if not self.head:
                        self.head = node(data=data)
                        return
                curr = self.head
                while curr.next:
                        curr = curr.next
                curr.next = node(data=data)

        # function to delete any node
        def delete_node(self, key):
                curr = self.head
                prev = None
                while curr and curr.data != key:
                        prev = curr
                        curr = curr.next
                if prev is None:
                        self.head = curr.next
                elif curr:
                        prev.next = curr.next
                        curr.next = None

        # function to get the last node
        def get_last_node(self):
                temp = self.head
                while(temp.next is not None):
                        temp = temp.next
                return temp.data

        # function to print the list nodes
        def print_list( self ):
                node = self.head
                while node != None:
                        print(node.data, end =" => ")
                        node = node.next


s = linked_list()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()

 
def binary_search(my_list, l, r, x):
        if r >= l:
                mid = l + (r - l)//2
                if my_list[mid] == x:
                        return mid
                elif my_list[mid] > x:
                        return binary_search(my_list, l, mid-1, x)
                else:
                        return binary_search(my_list, mid+1, r, x)
        else:
                return -1


nums = [ 2, 3, 4, 10, 40 ]
x = 10

print(binary_search(nums, 0, len(nums)-1,

#merge 
def merge(left, right):
        if not len(left) or not len(right):
                return left or right

        result = []
        i, j = 0, 0

        #merge the two parts into result[]
        while (len(result) < len(left) + len(right)):
                if left[i] < right[j]:
                        result.append(left[i])
                        i+= 1
                else:
                        result.append(right[j])
                        j+= 1
                if i == len(left) or j == len(right):
                        result.extend(left[i:] or right[j:])
                        break

        return result

def merge_sort(list):
        if len(list) < 2:
                return list

        mid = len(list)//2
        left = merge_sort(list[:mid])
        right = merge_sort(list[mid:])

        return merge(left, right)


a = [3,4,5,1,2,8,3,7,6]
print(merge_sort(a))

#quick sorte

from random import randint

def quicksort(lst, start, end):
        if start < end:
                pivot = randint(start, end)
                # swap with the last element
                lst[end],lst[pivot] = lst[pivot],lst[end]
                # partition the list
                split = partition(lst, start, end)
                # sort both halves
                quicksort(lst, start, split-1)
                quicksort(lst, split+1, end)

def partition(lst, start, end):
        pivot_index = start-1
        for index in range(start, end):
                # compare with pivot
                if lst[index] < lst[end]:
                        pivot_index = pivot_index + 1
                        # swap
                        lst[pivot_index],lst[index] = lst[index],lst[pivot_index]

        # swap with the last element           
        lst[pivot_index+1],lst[end] = lst[end],lst[pivot_index+1]

        return pivot_index+1


nums = [7,2,5,1,29,6,4,19,11]

quicksort(nums,0,len(nums)-1)

print(nums)

#insert sort
def insertion_sort(arr):
        for k in range(1, len(arr)):
                key = arr[k]
                j = k
                while j > 0 and arr[j-1] > arr[j]:
                        arr[j], arr[j-1] = arr[j-1], arr[j]
                        j = j - 1

my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print(my_list)

#selection sort
def selection_sort(arr):
        for k in range(len(arr)):
                min_index = k # smallest element
                for j in range(k + 1, len(arr)):
                        if arr[min_index] > arr[j]:
                                min_index = j
                arr[k], arr[min_index] = arr[min_index], arr[k]

nums = [64, 25, 12, 22, 11]
selection_sort(nums)
print(nums)

#tree algorith

class Node:
        def __init__(self, data):
                self.data = data
                self.left = None
                self.right = None

def print_tree(root, space=0, t=0):
        COUNT = 3

        if root is None:
                return

        space += COUNT

        print_tree(root.right, space, 1)

        for x in range(COUNT, space):
                print(" ",end = "")

        if t == 1 : # Right node
                print("/ ", root.data) 
        elif t == 2 : # Left node
                print("\ ", root.data)
        else: # Root node
                print(root.data)

        #Process left child
        print_tree(root.left, space, 2)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print_tree(root)


#add matrix with python
A = [[12,7,3],
        [4,5,6],
        [7,8,9]]

B = [[5,8,1],
        [6,7,3],
        [4,5,9]]

result = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]

for k in range(len(A)):
        for j in range(len(A[0])):
                result[k][j] = A[k][j]+B[k][j]

for r in result:
        print(r)

#Matrix multiplication
A = [[12,7,3],
        [4,5,6],
        [7,8,9]]

B = [[5,8,1,2],
        [6,7,3,0],
        [4,5,9,1]]

# result is 3x4
res = [[0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0]]

for l in range(len(A)):
        for j in range(len(B[0])):
                for k in range(len(B)):
                        res[l][j] += A[l][k] * B[k][j]

for r in res:
        print(r)

#hast table

class hash_table:
        def __init__(self):
                self.table = [None] * 127

        # Hash function
        def Hash_func(self, value):
                key = 0
                for i in range(0,len(value)):
                        key += ord(value[i])
                return key % 127

        def Insert(self, value):
                hash = self.Hash_func(value)
                if self.table[hash] is None:
                        self.table[hash] = value

        def Search(self,value):
                hash = self.Hash_func(value);
                if self.table[hash] is None:
                        return None
                else:
                        return hex(id(self.table[hash]))

        def Remove(self,value):
                hash = self.Hash_func(value);
                if self.table[hash] is None:
                        print("No Element found with value", value)
                else:
                        print("Element with value", value, "deleted")
                        self.table[hash] is None;


H = hash_table()
H.Insert("A")
H.Insert("B")
H.Insert("C")

print(H.Search("B"))

pos = 0


#linear search in python
def search(lst, n):
    i = 0
    
    while i < len(lst):
        if lst[i] == n:
            globals()['pos'] = i
            return True
        i += 1
        
    return False
    
    
    
lst_1 = [7, 9, 12, 4, 2, 10]
n = 4



if search(lst_1, n):
    print (' The number is found at index: ', pos)
else:
    print (' The number is not included in the list. ')

def linearSearch(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            print("Found it! It's at " + str(i) + " index")
            break
    else:
        print("Not found!")
lst_pass = [2,4,5,7,9]      #linear search should be done on a sorted list
linearSearch(lst_pass, 5)

#search
def search(list1,key):
    for i in range(len(list1 )):
        if key == list1[i]:
            print("Element found")
            break 

    else:
        print("Element  not found")

list1 = [23,43,56,76,83,90,21]
print(list1 )
key = int(input("Enter key element"))
search(list1,key)

#search
import sys
n=int(input())
arr=[]
def search(item,arr,l):
 for i in range(0,l):
  if(arr[i]==item):
   return i
  else:
   return -1
while True:
 try:
  x=int(input())
 except EOFError:
  break
 arr.append(x)
print(arr)
print(search(n,arr,len(arr)))

#search
def search(x, my_list):
      for k in range(len(my_list)):
        if my_list[k] == x:
        return k
  return -1
nums = [6,7,3,42,9]
print(search(42, nums))

#list node
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None
    
    # function to add a node at front
    def add_at_front(self, data):
        self.head = node(data=data, next=self.head)  

    # function to check whether the list is empty
    def is_empty(self):
        return self.head == None

    # function to add node at the end
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    
    # function to delete any node
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # function to get the last node
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # function to print the list nodes
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next


s = linked_list()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()

##deleted last node singel list 
class node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
        
class singlelist:
    def __init__(self):
        self.headval=None
        
    def printlist(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
            
    def removeend(self):
        removekey=self.headval
        prev=None
        
        while removekey.nextval is not None:
            prev=removekey
            removekey=removekey.nextval
            
        prev.nextval=None
        
            
        
list1=singlelist()
list1.headval=node("aditya")
e2=node("aditi")
e3=node("ajay")
e4=node("neha")

list1.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=None


list1.printlist()

print("\n")

list1.removeend()

list1.printlist()

#delete node from linked list 
class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return('%s > %s' % (self.data, self.next_node))

    def get_data(self):
        return self.data


node = Node(7, Node(14, Node(21, Node(28, Node(35, Node(42))))))
print(node)


def delete_node(node, key):
    previous_node = None
    while node is not None:
        if node.get_data() == key:
            print("found the key %s" % key)
            previous_node.next_node = node.next_node
            node = node.next_node
        else:
            previous_node = node
            node = node.next_node


delete_node(node, 28)
print(node)

#delete any node in single link list
class node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
        
class singlelist:
    def __init__(self):
        self.headval=None
        
    def printlist(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
            
    def removeend(self,removekey):
        removeend=self.headval
        
        while removeend is not None:
            if (removeend.dataval==removekey):
                break
            prev=removeend
            removeend=removeend.nextval
            
        prev.nextval=removeend.nextval
        removeend=None
            
        
list1=singlelist()
list1.headval=node("rana")
e2=node("perro")
e3=node("rana")
e4=node("loro")

list1.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=None


list1.printlist()

print("\n")

list1.removeend("loro")

list1.printlist()

#INSERT of node at middle 

class node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
        
class singlelist:
    def __init__(self):
        self.headval=None
        
    def printlist(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
            
    def AtMiddle(self,newdata,middle_node):
        newnode=node(newdata)
        middle=self.headval
        if middle is None:
            headval.nextval=newnode
            newnode.nextval=None
            
        newnode.nextval=middle_node.nextval
        middle_node.nextval=newnode
        
            
list1=singlelist()
list1.headval=node("loro")
e2=node("perro")
e3=node("carro")
e4=node("casa")

list1.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=None

list1.printlist()
print("\n")

list1.AtMiddle("raya",list1.headval.nextval)
list1.printlist()