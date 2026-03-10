from analyzer import folder_analyzer
from cleaner import remove_empty_folders
from manager import organize_files


def main():
    path = str(input("Write the path: "))
    if path is None:
        raise ValueError("Write the correct path")

    results_analyzer = folder_analyzer(path)
    print("\n-------------------------------------------------------------------------")
    print("\nThese are the data from " + path + ":")
    print("\n-------------------------------------------------------------------------")
    for ext, amount in results_analyzer:
        print(ext, amount)
    print("\n-------------------------------------------------------------------------")
    print("\n                       Organizing analyzed files")
    print("\n-------------------------------------------------------------------------")
    if organize_files(path):
        print(f"\nSuccess! The new files have been organized in '{path}'")
    else:
        print("\nThe folder was already completely organized. No files were moved.")
    print("\n-------------------------------------------------------------------------")
    print("\n                       Deleting empty folders")
    print("\n-------------------------------------------------------------------------")
    cleaner_option = input("\nDo you want to clean the empty folders? YES/NO:").strip().upper()
    if cleaner_option == 'YES':
        if remove_empty_folders(path):
            print("\nCleanup complete!")
        else:
            print("\nNo empty folders found to delete.")
    elif cleaner_option == 'NO':
        print("\nThanks for use my tool :)")
    else:
        print("\nWrite YES or NO")

if __name__ == '__main__':
    main()