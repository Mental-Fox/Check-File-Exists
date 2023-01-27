import os


def check_file_exists(curdir, name_file, size_file):
    # The function goes through the files in the current folder
    for root, dirs, files in os.walk(curdir):
        for file in files:
            print(file)
            # if the name is in the files and if this file exists and is not equal to !=0
            if name_file in file:
                if os.path.exists(file) and os.stat(file).st_size != 0:
                    # if the size is less than specified then True if not then False
                    if os.path.getsize(file) < size_file:
                        return True
                    else:
                        return False


curdir = os.path.abspath(os.curdir) + "\\"
size_file = 3000000
name_file = "ref"

test_var = check_file_exists(curdir, name_file, size_file)
print(test_var)
