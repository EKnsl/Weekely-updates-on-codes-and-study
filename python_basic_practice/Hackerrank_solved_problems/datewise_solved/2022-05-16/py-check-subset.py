# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
Given T , the number of test cases
for each test case,
    given two set of numbers as input
    outputs if the first set is subset of the second one 
"""

T = int(input())
for cases in range(T) :
    n = int(input())
    num_list = [int(x) for x in input().split()]
    # print(set(num_list))
    A = set(num_list)
    
    n = int(input())
    num_list = [int(x) for x in input().split()]
    # print(set(num_list))
    B = set(num_list)
    
    # print(A,B)
    print(A.issubset(B))
    
