
# Author: Mujtaba
# Date: July 21, 2023

# Module that scrapes data from the txt files in /rawtxt directory and adds to dataset


import os
from architecture import Module

from data_writer import *

rawtxt_directory = "./rawtxt/"

class RawTxtScrap(Module):
    def __init__(self):
        Module.modules.append(self)
    
    # read all files in rawtxt directory and convert it into paragraphs containing 1000 words each
    def render(self):
        file_list = os.listdir(rawtxt_directory)

        for file_name in file_list:
            file_path = os.path.join(rawtxt_directory, file_name)

            with open(file_path, 'r') as file:
                content = file.read()
                write2dataset(content, file_name="english_words.txt")
