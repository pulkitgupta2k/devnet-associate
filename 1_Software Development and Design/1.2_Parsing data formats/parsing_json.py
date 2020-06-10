import json
from pprint import pprint

with open("address_list.json") as f:
    json_dic = json.load(f)
pprint(json_dic)

print("")

str_dic = """ {"key_1": "value_1", "key_2": "value_2"} """
json_dic = json.loads(str_dic)
pprint(json_dic)

with open("test_copy.json", "w") as f:
    json.dump(json_dic, f)