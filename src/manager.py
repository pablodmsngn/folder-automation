import os
import shutil


def get_target_path(extension: str, destinations: dict) -> str:
    for path, extensions in destinations.items():
        if extension.lower() in extensions:
            return path
    return 'escritorio2/others'

def resolve_duplicate(target_folder: str, filename: str) -> str:
    base_name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(target_folder, new_filename)):
        new_filename = f"{base_name}_{counter}{ext}"
        counter += 1
    return new_filename

def organize_files(folder_path: str, config: dict) -> bool:
    if not config:
        return False
    moved_count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            item_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            if not ext:
                continue
            relative_path = get_target_path(ext, config)
            target_folder = os.path.join(folder_path, os.path.normpath(relative_path))
            if root == target_folder:
                continue
            os.makedirs(target_folder, exist_ok=True)
            safe_filename = resolve_duplicate(target_folder, file)
            destination_path = os.path.join(target_folder, safe_filename)
            shutil.move(item_path, destination_path)
            moved_count += 1
    if moved_count == 0:
        return False
    return True
