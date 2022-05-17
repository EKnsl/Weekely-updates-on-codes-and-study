if __name__ == '__main__':
    N = int(input())
    
    values = []
    
    for i in range(N) :
        command = list(input().split() )
        operation = command[0]
        
        if operation == 'insert' :
            index , value = int(command[1]) , int(command[2])
            values.insert(index, value)
        
        elif operation == 'print' :
            print(values)
        
        elif operation == 'remove' :
            element = int(command[1])
            
            if element in values :
                values.remove(element)
        
        elif operation == 'append' :
            value = int(command[1])
            values.append(value)
        
        elif operation == 'sort' :
            values.sort()
        
        elif operation == 'pop' :
            if len(values) > 0 :
                values.pop() 
        
        elif operation == 'reverse' :
            values.reverse()
        

            
            
     
