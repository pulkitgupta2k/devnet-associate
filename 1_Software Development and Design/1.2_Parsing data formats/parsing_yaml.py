import yaml

with open("address_list.yaml") as f:
    yaml_dic = yaml.safe_load(f)

with open("test.yaml", "w") as f:
    yaml.dump(yaml_dic, f)

print(yaml_dic)