import json

json_string = '{"aaaa": 1, "bbb": 2, "ccc": 3}'
dict_obj = json.loads(json_string)
array = []
for i in dict_obj.items():
    array.append(i)

array.sort(key=lambda x: -x[1])
print(array)





