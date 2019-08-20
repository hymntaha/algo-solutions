#This is a great example of a divide and conquer strategy.

def binarySearch(list, item):
    first = 0
    last = len(list) -1
    found  = False

    while first <= last and not found:
        midpoint = (first+last) // 2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint+1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 32))

# Recursion version

def BinarySearchRecursive(list, key):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == key:
            return True
        else:
            if key < list[midpoint]:
                return BinarySearchRecursive(list[:midpoint])
            else:
                return BinarySearchRecursive(list[midpoint:])

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(BinarySearchRecursive(testlist, 32))

# Time Complexity is O(logn)
