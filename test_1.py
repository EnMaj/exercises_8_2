text = input()
i,j = map(int, input().split(" "))
if i == 0:
    i += 1
out_filter = list(filter(lambda x: x.isupper(), text[i-1:j]))
print(len(out_filter))