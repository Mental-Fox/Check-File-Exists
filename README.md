**Check File Exists**


```
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
```


Rus: Функция проходится в текущей папке по файлам если имя есть в файлах и если этот файл существует и не равен !=0 и если размер меньше чем указали то True если нет то False
