from functools import cmp_to_key

def compare(student1 , student2) :
    
    name1 , name2 = student1[0], student2[0]
    score1, score2 = student1[1] , student2[1]
    
    epsilon = 10 ** -9
    
    if abs(score1 - score2) < epsilon :
        return name1 < name2
    
    else :
        return score1 < score2

        
if __name__ == '__main__':
    
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    # sorting strudents record based on lowest to highest score and then based on names in alphabetic order
    records = sorted(records, key=cmp_to_key(compare))
    
    unique_scores = list(set(score for name , score in records) )
    
    #as python set() is not sorted , we need to sort list to get ordered set
    sorted_scores = sorted(unique_scores)
    
    second_lowest = sorted_scores[1] 
    
    names = list(name for name , score in records if score == second_lowest)
    
    for name in sorted(names) :
        print(name)
    
    
    
    
    
        
        
        
        
    
        
        
