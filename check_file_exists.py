import os


def check_file_exists(curdir, name_file, size_file):
    for root, dirs, files in os.walk(curdir):
        for file in files:
            print(file)
            if name_file in file:
                if os.path.exists(file) and os.stat(file).st_size != 0:
                    if os.path.getsize(file) < size_file:
                        return True
                    else:
                        return False


curdir = os.path.abspath(os.curdir) + "\\"
size_file = 3000000
name_file = "clesh"

test_var = check_file_exists(curdir, name_file, size_file)
print(test_var)
