from functools import reduce

a,b,c = map(int, input().split(" "))
array = list(range(a,b+1))
new_array = list(map(lambda x: x if (int(x**0.5))**2 == x and x%c == 0 else 1, array))
result = reduce(lambda x,y: x * y, new_array)
print(result)