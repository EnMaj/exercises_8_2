a,b,c,d = map(int, input().split(" "))
array = list(range(a,b+1))
out_filter = sum(filter(lambda x: x%c == 0 and x%d == 0, array))
print(out_filter)