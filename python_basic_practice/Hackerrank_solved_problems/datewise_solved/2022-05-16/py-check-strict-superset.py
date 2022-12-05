# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
Given a set A as superset and n sets
This program checks if set A is superset of the other n sets
"""
#input a list of integers
num_list = [int(x) for x in input().split()]
# print(num_list)

#convert list of integers to set()
A = set(num_list)

n = int(input())
is_superset = True

for i in range(n) :
    num_list = [int(x) for x in input().split()]
    #output will be false if given set A is not superset of any of the n sets  
    if A.issuperset(set(num_list) ) == False :
        is_superset = False
    
print(is_superset)
    
    
