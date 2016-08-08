# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(data):
    if data == []:
        return None
    res, length = [], []
    n, m = 0, 0
    res.append([data.pop(0)])
    while n != len(data):
        if data[n] == res[-1][0]:
            res[-1].append(data[n])
        if data[n] != res[-1][0]:
            res.append([data[n]])
        n += 1
    while m != len(res):
        length.append(len(res[m]))
        m += 1
    a = length.index(max(length))
    return res[a][0]



#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

