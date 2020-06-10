# import xml.etree.ElementTree as ET
from lxml import etree as ET # extension of element tree

def method_lxml():
    with open("address_list.xml") as f:
        xml_etree = ET.parse(f)
        roots = xml_etree.getroot()
        for root in roots:
            print(ET.tostring(root))
            print(root.get("Id"))

######################################################

import xmltodict
from pprint import pprint

def method_xmltodict():
    with open("address_list.xml") as f:
        xml_dicts = xmltodict.parse(f.read())
        pprint(xml_dicts)
        print("")
        for xml_dict in xml_dicts['root']['addresses']:
            print(xml_dict)

#####################################################

if __name__ == "__main__":
    method_lxml()
    method_xmltodict()