#complexities
#1) Constant Time - O(1)
#2) Logarithmic Time - O(log n)
#3) Linear Time - O(n)
#4) Quasilinear Time - O(n log n)
#5) Quadratic Time - O(n^2)
#6) Exponential Time - O(x^n)
#7) Factorial Time - O(n!)

#Space complexity: it is the memory required by an algorithm until it executes completely.
# basically from start to stop of the algorithm

#Algorithmic Thinking : approach to problem solving that involves breaking a problem down into
# a clearly defined input and output
# along with a distinct set to steps that solves problems by going from input to output

#-----------------------------------------------------------

def linear_search(list, target):  # algorthm runs in linear time
    for i in range(0, len(list)):
        if list[i] == target:
            return i

        return None

#-----------------------------------------------------------
# block of code: must return a value, must complete execution in a finite time, must output same result for a given input
#-----------------------------------------------------------

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")

#-----------------------------------------------------------

def binary_search(list, target): #logarithmic time complexity - worst case
    #Space complexity : Constant Time

    first = 0
    last = len(list) - 1 #constant time

    while first <= last: #logarithmic - worst case
        midpoint = (first + last)//2 #constant operations
        if list(midpoint) == target:
            return midpoint
        elif list(midpoint) < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

#-----------------------------------------------------------

def recursive_binary_search(list, target):
    #creating new lists every time for every recursion
    #Both Time AND Space complexity : Logarithmic

    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

#-----------------------------------------------------------

listy = [1, 5, 8, 9, 10, 17, 20, 40, 65]
recursive_binary_search(listy, 40)

