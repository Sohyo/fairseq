import xml.etree.ElementTree as ET
from typing import Dict
import xmltodict
import pandas as pd
import sys
import csv

'''
In this file, the alignment information file so-called xces file will be splited to several files which contain alignment info of only one document.
These files will be used to extract plain sentences from the xml files by OPUS tool.
'''

csv.field_size_limit(sys.maxsize)


# read file and save it as array
def text2arr(text_path):
    with open(text_path) as f:
        arr_from_text = [line.rstrip() for line in f]
    return arr_from_text


def arr2txt(arr, file_name):
    with open("custom_split_data/"+file_name, "w") as txt_file:
        for line in arr:
            txt_file.write("".join(line) + "\n")


def xml2dict(xml_path):
    with open(xml_path) as fd:
        orig_align_dict= xmltodict.parse(fd.read())
    return orig_align_dict


def split_dict2xml(xml_path):
    with open(xml_path) as fd:
        orig_align_dict = xmltodict.parse(fd.read(), process_namespaces=True)

    document_num = 0  # the splitted xces files will be counted from 0.

    for document in orig_align_dict['cesAlign']['linkGrp']:
        document = {'linkGrp': document}
        out = xmltodict.unparse(document, pretty=True)
        with open("orig/EMEA_orig/xces_files/" + str(document_num) + ".xml", 'a') as file:
            file.write(out)
        document_num += 1


xml_path = "orig/EMEA_orig/de-en.xml"

split_dict2xml(xml_path)