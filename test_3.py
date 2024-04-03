a,b,c,d = map(int, input().split(" "))
array = list(range(a,b+1))
sum_number = sum(map(lambda x:1 if x!= c and x%10 == d else 0, array))
print(sum_number)