# Fibonnaci sequence

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(20))

# Fibonnaci sequence Memoized

def fib2(m, q={}):
    if m <= 1:
        return m
    if m in q:
        return q[m]
    q[m] = fib2(m-1,q) + fib2(m-2,q)
    return(q[m])

print(fib2(20))

# Find lowest number in array

array1 = [8,10,20,4,23,1,9,44,0]
print(min(array1))

# Finding out the algorithm for the same damn thing
array2 = [8,10,20,4,23,1,9,44,0]
smol = array2[0]
for i in array2:
    if i < smol:
        smol = i
print(smol)

# Bubble sort
# Traverses the whole array and sorts them based on index and value
k = len(array2)
for h in range(k-1):
    for b in range(k-h-1):
        if array2[b] > array2[b+1]:
            array2[b], array2[b+1] = array2[b+1],array2[b]

print(array2)

# Improved bubble sort
myarray = [1,0,9,8,0.1,12,900,10024124,5,2,123,436543,67]
p = len(myarray)
for a1 in range(p-1):
    swapped = False
    for x in range(p-a1-1):
        if myarray[x] > myarray[x+1]:
            myarray[x], myarray[x+1] = myarray[x+1], myarray[x]
            swapped = True
    if not swapped:
            break

print(myarray)

# Linear search

def linearSearch(val, arr=[]) -> int:
    for i in range(0,len(arr),1):
        if(arr[i] == val):
            return i
    return -1

print(linearSearch(12, [1,20,30,600,40,12,25]))