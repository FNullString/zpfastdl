import os

# 获取当前目录的绝对路径
current_dir = os.getcwd()

# 获取当前目录下的所有文件和子目录
all_items = os.listdir(current_dir)

# 过滤出文件（不包括子目录）
files = [item for item in all_items if os.path.isfile(os.path.join(current_dir, item))]

# 将当前目录的绝对路径与文件名拼接
file_paths = [os.path.join(current_dir, file) for file in files]

# 打印所有文件的完整路径
for i in range(0, len(file_paths)):
    file_paths[i] = file_paths[i].split('patch2\\')[1]
    file_paths[i] = file_paths[i].replace('\\', '/')
    print(file_paths[i])
