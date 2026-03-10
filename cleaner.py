import os


def remove_empty_folders(folder_path: str) -> bool:
    deleted_count = 0
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    deleted_count += 1
            except OSError as e:
                print(f"Warning: Could not delete folder '{dir_path}'. Error: {e}")
    if deleted_count == 0:
        return False
    return True