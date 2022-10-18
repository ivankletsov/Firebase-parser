import os
dir_path = r'/Users/egor/Documents/data/'
count = 0
folder = os.listdir(dir_path)
for path in folder:
#check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
        print(count)
print('File count:', count)