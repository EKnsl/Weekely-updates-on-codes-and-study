""" 
Given a set and number of operations toperform.
for each operation,  name of the operation, size and the elements 
These number of sets have to perform some specific mutation operations on given set
based on another given set, This program prints the sum of elements in the first set 
after performing all the given mutation operations

input : 
The first line contains the number of elements in the first set.
The second line contains the space separated list of elements in the first set.
The third line contains an integer , the number of opearions to perform.
The next lines are divided into parts containing two lines each.
The first line of each part contains the space separated entries of the operation name 
and the size of the other set.
The second line of each part contains space separated list of elements in the other set.

output :
sum of elements i the first set after performing all the operations
"""

def perform_operation(operation_name, set1, set2) :
    if operation_name == "intersection_update" :
        set1.intersection_update(set2)
    
    elif operation_name == "update" :
        set1.update(set2)
    
    elif operation_name == "symmetric_difference_update" :
        set1.symmetric_difference_update(set2)
    
    elif operation_name == "difference_update" :
        set1.difference_update(set2)
    
if __name__ == '__main__':
    n = int(input())

    set1 = set(map(int, input().split()))

    cnt_op = int(input())
        
    for i in range(cnt_op) :
        operation_name , set2_size = input().split()
        set2_size = int(set2_size)
            
        set2 =  set(map(int, input().split()))
            
        perform_operation(operation_name, set1, set2)
        
        print(sum(set1) )
        