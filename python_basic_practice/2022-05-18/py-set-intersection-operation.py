
"""
Given the dimensions and elements present in two set of integers, 
this program finds number of elements in the set of  elements 
that are either present in first set or in second

input:
The first line contains n, the number of students who have subscribed to the English newspaper.
The second line contains space separated roll numbers of those n students.
The third line contains m, the number of students who have subscribed to the French newspaper.
The fourth line contains space separated roll numbers of those m students.

output :
total number of students who have subscriptions to both English and French newspapers.

"""

if __name__ == '__main__':
    
    #input an integer
    n = int(input().strip())
    # print(n)
    
    #input a set of integers
    set1 = set(map(int, input().split()))
    # print(set1)
    
    m = int(input().strip())
    # print(m)
    
    #input a set of integers
    set2 = set(map(int, input().split()))
    # print(set2)
    
    #prints number of elements common in two sets set1 and set2
    print(len(set1.intersection(set2) ) )
    
    