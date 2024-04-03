import json

def to_json(func):
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped

@to_json
def json_format(parametr):
    return {'data': parametr}

print(json_format('a'))
print(json_format(['a','b','c']))
print(json_format({'abv':'cde', 'qqqq':{'aaaaa':['a','b','c','d']}}))