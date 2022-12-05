# Enter your code here. Read input from STDIN. Print output to STDOUT

n , m = map(int, input().split())

arr = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))
# print(arr)

total_happiness = 0
for val in arr :
    if val in A :
        total_happiness += 1
    elif val in B:
        total_happiness -= 1

print(total_happiness)
        
