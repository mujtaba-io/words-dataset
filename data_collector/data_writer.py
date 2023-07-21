

# Author: Mujtaba
# Date: July 21, 2023

# Ensure that passed string of words are lowercased, stripped of punctuation, and split into a list of words,
# no duplication of words in dataset, and so on. - Provides write2dataset() method to be called by Module class
# which simply passes chunks of strings/paragraphs in raw form.


import re


data_folder = "./data/"


def refine_input_text(content: str) -> str:
    content = content.lower()
    # replace all non-alphanumeric characters with empty
    content = re.sub(r'[^a-z0-9]', ' ', content)
    # replace all whitespace characters with single space
    content = re.sub(r'\s+', ' ', content).strip()

    # Remove standalone numbers while preserving numbers within words
    content = re.sub(r'\b\d+\b(?!-)', '', content)

    return content


def remove_duplicate_words_in_file(file):
    with open(file, 'r') as f:
        content = f.read()
    words = content.split()
    unique_words = set()
    for word in words:
        unique_words.add(word)

    with open(file, 'w') as f:
        f.write('\n'.join(unique_words))




def write2dataset(content: str, file_name: str = "no_language_specified_dataset.txt"):
    print("Writing to dataset...")
    content = refine_input_text(content)

    words = content.split(' ')

    with open(data_folder + file_name, 'a') as file:
        for word in words:
            file.write(word + '\n')
    remove_duplicate_words_in_file(data_folder + file_name)
    


