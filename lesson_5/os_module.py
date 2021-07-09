import os

#change working directory
# print(os.getcwd())
# print(os.chdir("../lesson_4"))
# print(os.getcwd())

# how much cores in CPU
# print(os.cpu_count())

# get current active login
# print(os.getlogin())

# get content of directory in DirEntry objects
# for item in os.scandir("."):
#     print(item)

# get content of current directory as list of string names files and folders
# print(os.listdir())

# create directory in current directory
# for _ in range(10):
# os.mkdir(f"new_1")

# create directory tree
# os.makedirs("A/B")

# remove directory if it is empty
# os.rmdir("A")

# remove folder with content even if not empty
# import shutil
# shutil.rmtree("/home/local/DO/mykyta.lymarchuk/PycharmProjects/python_course/lesson_5/A")

# remove file
# os.remove("text.txt")

# execute own custom scripts
# print(os.system("mkdir new"))
# os.system("rmdir new")

# os.getcwd()
# os.chdir("/home/local/DO/mykyta.lymarchuk/PycharmProjects")
# os.makedirs("a/b/c/d")



# get information about directory and all child leafs
for dirpath, dirname, filename in os.walk('.'):
    print('Current path: ',dirpath)
    print('Directories: ', dirname)
    print('Files: ', filename)
    print()