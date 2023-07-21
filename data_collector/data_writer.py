

# Author: Mujtaba
# Date: July 21, 2023

# Ensure that passed string of words are lowercased, stripped of punctuation, and split into a list of words,
# no duplication of words in dataset, and so on. - Provides write2dataset() method to be called by Module class
# which simply passes chunks of strings/paragraphs in raw form.


import re


data_folder = "./data/"


def refine_text(content: str) -> str:
    content = content.lower()
    # replace all non-alphanumeric characters with empty
    content = re.sub(r'[^a-z0-9]', ' ', content)
    # replace all whitespace characters with single space
    content = re.sub(r'\s+', ' ', content).strip()
    return content


def write2dataset(content: str, file_name: str = "no_language_specified_dataset.txt"):
    print("Writing to dataset...")
    content = refine_text(content)
    print(content)

    words = content.split(' ')

    # check if the word is not already in the file_name, add it, else ignore it each word is on a new line
    file_content = ''
    with open(data_folder + file_name, 'r') as r_file:
        file_content = r_file.read()

    with open(data_folder + file_name, 'a') as file:
        for word in words:
            if word not in file_content:
                file.write(word + '\n')


