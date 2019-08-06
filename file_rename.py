"""
rename file from a folder
Get: http:icarus.cs.weber.edu/~hvalle/hafb/prank.zip
"""

import os
def rename_files():
    """
    rename files in folder
    :return:
    """
    folder_dir = r"C:\Users\keithmoore1.AD\Desktop\HAFB\prankOrig"
    files = os.listdir(folder_dir)
    save_path = os.getcwd() # current working directory
    for file in files:
        #remove digits from name
        new_file = file.lstrip("0123456789")
        print(file, " - ", new_file)
        # rename filename
        os.chdir(folder_dir)
        os.rename(file,new_file)
    # get back home
    os.chdir(save_path)


def main():
    """
    test function
    :return: nohing
    """
    rename_files()

if __name__ == '__main__':
    main()
    exit(0)