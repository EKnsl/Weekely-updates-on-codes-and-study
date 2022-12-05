from collections import defaultdict

k = int(input())

num_list = list(map(int, input().split() ) )

freq = defaultdict(int)

for elem in num_list :
    freq[elem] += 1

# print(freq)

for val , cnt in freq.items() :
    # print(key, value)
    if cnt == 1 : 
        print(val)
        break;

