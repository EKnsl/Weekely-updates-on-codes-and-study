
"""
Given the dimensions and elements present in two set of integers, 
this program finds number of elements in difference of the two sets i.e. , 
number of elements that are either present in the first set, but not in the second one
or present in the second set, but not in the first one

input:
The first line contains n, the number of students who have subscribed to the English newspaper.
The second line contains space separated roll numbers of those n students.
The third line contains m, the number of students who have subscribed to the French newspaper.
The fourth line contains space separated roll numbers of those m students.

output :
number of elements that are either present in the first set, 
but not in the second one or 
present in the second set, but not in the first one

"""
#returns set of elements that are either present 
# in first set or in second, but not in both
def symmetric_difference(A , B) :
    A_and_notB = A.difference(B)
    B_and_notA = B.difference(A)
    return A_and_notB.union(B_and_notA)

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
    
    #prints set of elements that are either present 
    # in first set or in second, but not in both
    print(len(symmetric_difference(set1,set2) ) )
    
    