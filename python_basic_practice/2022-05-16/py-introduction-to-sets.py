def average(array):
    # your code goes here
    height_set = set(array)
    cnt_distinct = len(height_set)
    avg_height = float(sum(height_set))/cnt_distinct
    
    #return average hieght rounded to 3 places after the decimal
    return round(avg_height , 3) 

if __name__ == '__main__':
    n = int(input())
    
    #take whole iline as input and convert it to a list of integers
    arr = list(map(int, input().split()))
    
    #takes list of integers nad compute and store average value of the unique numbers in the list
    result = average(arr)
    
    print(result)