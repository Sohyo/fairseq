import xml.etree.ElementTree as ET
from typing import Dict
import xmltodict
import pandas as pd
import sys
import csv

'''
    Temporary file to save some old codes for just in case.
'''
xml_path = "orig/EMEA_orig/de-en.xml"
with open(xml_path) as fd:
    orig_align_dict = xmltodict.parse(fd.read(), process_namespaces=True)
document_num = 0    # the splitted xces files will be counted from 0.
for document in orig_align_dict['cesAlign']['linkGrp']:
    document = {'linkGrp': document}
    out = xmltodict.unparse(document, pretty=True)
    with open("orig/EMEA_orig/xces_files/"+str(document_num)+".xml", 'a') as file:
        file.write(out)
    document_num+=1


# # make a 'root' to the splitted xml files - because it complains that there is no 'root'.
# example = {'linkGrp': example}
# out = xmltodict.unparse(example, pretty=True)
# with open("orig/EMEA_xml/xces_files/example.xml", 'a') as file:
#     file.write(out)



# for file in orig_align_dict['cesAlign']['linkGrp']:
#     print('=================================================== /n')
#     print(file)
#
# ########################################3
# xml = open(path, "r")
# org_xml = xml.read()
# dict_xml = xmltodict.parse(org_xml, process_namespaces=True)
#
# out = xmltodict.unparse(dict_xml, pretty=True)
# with open("path/new.qml", 'a') as file:
#     file.write(out.encode('utf-8'))

# xmlfile_dict = xmltodict.parse(xml_path)
# print(xmlfile_dict)