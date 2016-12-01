import os
import unotools

def print_current_file_path():
    print(os.getcwd()+ "\n")

    print(__file__ + "\n")

    full_path = os.path.realpath(__file__)
    print(full_path + "\n")