
"""
Given the dimensions and elements present in two set of integers, 
this program finds their symmetric difference, 
i.e, elements that are either present in first set or in second, but not in both

input:
n : integer denoting number of elements of the first set,
a : set of integers
m : integer denoting number of elements of the first set,
b : set of integers

output :
set of all elements that are either present in first set or in second, but not in both

"""

#returns set of all elements that are either present 
# in first set or in second, but not in both in ascending order
def symmetric_difference_ordered(A , B) :
    A_and_notB = A.difference(B)
    B_and_notA = B.difference(A)
    
    return sorted(A_and_notB.union(B_and_notA))

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
    
    # set of all elements that are either present 
    # in first set or in second, but not in both in ascending order
    
    ordered_symmetric_dif = symmetric_difference_ordered(set1 , set2)
    
    #print elements in the ordered_symmetric_dif one per line 
    for x in ordered_symmetric_dif :
        print(x) 
    
    
    
    
    
    
    