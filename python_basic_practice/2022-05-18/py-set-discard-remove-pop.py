
"""
Given the number of elements and elements present in a set, and some operations 
this program prints number of elements present in the set after  performing operatoins on the set

input:
The first line contains n, the number of elements in the set.
The second line contains space separated elements of the set.
The third line contains m, the number of operationsto perform.
Each of the next m line contains a string denoting the operation.

output :
sum of elements in the set after performing m operations.

"""

def perform_operation(S, operation) :
    
    line = operation.split()
    
    command = line[0]
    #pops a random element from set S if S is not empty    
    
    if command == "pop" :
       if len(S) > 0 :
           S.pop() 
    
    #removes given elemeent for set S, 
    # raises erro if element is not present in the set
    elif command == "remove" :
        elem = int(line[1].strip())
        S.remove(elem) 
        
    #discards given elemeent for set S
    elif command == "discard" :
        elem = int(line[1].strip())
        S.discard(elem)
        
        
if __name__ == '__main__':
    
    #input an integer
    n = int(input().strip())
    # print(n)
    
    #input a set of integers
    S = set(map(int, input().split()))
    # print(set1)
    
    #input number of operation to perform
    m = int(input().strip())
    # print(m)

    #input m opearions and perform opearion on set S
    for i in range(m) :
        operation = input()
        # print(operation)
        perform_operation(S, operation)
    
    #print sum of elements in S after performing m operations
    print( sum(S) )
    
    