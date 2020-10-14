from os import listdir
from os.path import isfile, join
import os
import sys
# dir_path = os.path.dirname(os.path.realpath(__file__))
# parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
# sys.path.insert(0, parent_dir_path)

from soyo.get_split_xml_per_doc import split_into_src_trg
from soyo.split_dataset import split_arr
from soyo.util import get_sorted_file_list


def main():

    root_dir_EMEA = "/home/diego/PycharmProjects/my_fairseq/soyo/orig/EMEA_orig/xmlfiles_per_doc/"
    xml_file_list = get_sorted_file_list(root_dir_EMEA)

    for file in xml_file_list:
        print(root_dir_EMEA+file)
        #split_into_src_trg(root_dir_EMEA+file)


if __name__ == "__main__":
    main()