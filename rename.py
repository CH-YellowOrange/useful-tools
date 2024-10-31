import os

# 目标目录路径
parent_directory = "E:\\cvpr\\html\\vessel_graph_generation\\datasets\\dataset_18_June_2023\\"

# 初始化计数器用于重命名
counter = 1

# 遍历父目录中的所有文件夹
for folder_name in os.listdir(parent_directory):
    folder_path = os.path.join(parent_directory, folder_name)

    # 检查是否为文件夹
    if os.path.isdir(folder_path):
        # 构造新的文件夹名
        new_folder_name = f"folder_{counter}"
        new_folder_path = os.path.join(parent_directory, new_folder_name)

        # 重命名文件夹
        os.rename(folder_path, new_folder_path)

        print(f"Renamed: {folder_name} -> {new_folder_name}")

        # 增加计数器
        counter += 1
