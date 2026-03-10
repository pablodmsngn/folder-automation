import os
from collections import Counter


def folder_analyzer(folder_path):

    extensions_with_amount = extensions_extraction(folder_path)
    return extensions_with_amount

def extensions_extraction(folder_path):
    extensions = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            ext = os.path.splitext(file)[1]
            extensions.append(ext)
    return data_extraction(Counter(extensions))


def data_extraction(counter):
    data = []
    for ext, amount in counter.items():
        data.append([ext, amount])
    return data