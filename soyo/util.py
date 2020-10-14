from os import walk, listdir
from os.path import isfile, join


def get_sorted_file_list(files_path):
    xces_file_list = [f for f in listdir(files_path) if isfile(join(files_path, f))]
    # xces_file_list.sort(key=lambda f: int(f[:-4]))
    xces_file_list.sort(key=lambda f: int(filter(str.isdigit, f)))
    return xces_file_list


