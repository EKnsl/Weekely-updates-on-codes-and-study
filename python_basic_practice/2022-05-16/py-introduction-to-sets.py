def average(array):
    # your code goes here
    height_set = set(array)
    cnt_distinct = len(height_set)
    avg_height = float(sum(height_set))/cnt_distinct
    
    #return average hieght rounded to 3 places after the decimal
    return round(avg_height , 3) 

if __name__ == '__main__':
    n = int(input())
    
    #input whole line , split into tokens basen on space , convert them into integers and store them in a list
    arr = list(map(int, input().split()))
    
    #given a list of integers as input, computes average of the distinct integers 
    result = average(arr)
    
    print(result)