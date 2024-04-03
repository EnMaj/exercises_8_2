import json
import xmljson
import yaml
import xmltodict

def to_format(parametr = None):
    def to_json(func):
        def wrapped(*args, **kwargs):
            if parametr == 'xml':
                result = xmltodict.unparse(func(*args, **kwargs))
            elif parametr == 'yaml':
                result = yaml.dump(func(*args, **kwargs))
            elif parametr == None or parametr == 'json':
                result = json.dumps(func(*args, **kwargs))
            return result
        return wrapped
    return to_json


@to_format('xml')
def json_format(parametr):
    #return {'data': parametr}
    return {"Response": {"TransactionId":"12345","ResultCode": "0","Fields": {"field1": {"name": "LegalCode","text": "4"}}}}

print(json_format('a'))
print(json_format(['a','b','c']))
print(json_format({'abv':'cde', 'qqqq':{'aaaaa':['a','b','c','d']}}))