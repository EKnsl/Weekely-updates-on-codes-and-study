# Enter your code here. Read input from STDIN. Print output to STDOUT

#this program takes name of n cities and prints number of unique names

n = int(input())
# print(n)

countrySet = set()
for i in range(n) :
    country_name = input()
    countrySet.add(country_name)

print(len(countrySet) )
