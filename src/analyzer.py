import os
from collections import Counter


def folder_analyzer(folder_path):
    return extensions_extraction(folder_path)


def extensions_extraction(folder_path):
    ext_counter = Counter()
    scanned_files = 0
    ignored_dirs = {'$RECYCLE.BIN', 'System Volume Information', '.git', 'node_modules', '__pycache__'}
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for file in files:
            try:
                ext = os.path.splitext(file)[1].lower()
                if ext:
                    ext_counter[ext] += 1
                scanned_files += 1
                if scanned_files % 5000 == 0:
                    print(f"  ... {scanned_files} files analyzed ...")
            except Exception:
                continue
    return data_extraction(ext_counter)


def data_extraction(counter):
    data = []
    for ext, amount in counter.items():
        data.append([ext, amount])
    return data