import json
import xmljson
import yaml

def to_format(parametr = None):
    def to_json(func):
        def wrapped(*args, **kwargs):
            result = json.dumps(func(*args, **kwargs))
            if parametr == 'xml':
                result = xmljson.badgerfish.etree(result)
            elif parametr == 'yaml':
                result = yaml.dump(result,allow_unicode=True)
            return result
        return wrapped
    return to_json


@to_format('yaml')
def json_format(parametr):
    return {'data': parametr}

print(json_format('a'))
print(json_format(['a','b','c']))
print(json_format({'abv':'cde', 'qqqq':{'aaaaa':['a','b','c','d']}}))