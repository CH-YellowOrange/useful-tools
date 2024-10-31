import os
import shutil

# 原始文件夹路径
source_folder = "E:\\cvpr\\html\\vessel_graph_generation\\datasets\\dataset_18_June_2023\\"
# 目标文件夹路径
destination_folder = "E:\\cvpr\\dataset\\"

# 创建目标文件夹（如果不存在）
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 指定要查找的文件名模式（例如，所有名为 "target_name.jpg" 的图片）
target_name = "art_ven_img_gray.png"

# 初始化计数器用于重命名
counter = 1



# 遍历源文件夹中的文件
for filename in os.listdir(source_folder):
    print (filename)
    temp = ""
    temp = source_folder + filename +"\\"
    print(temp)
    # 检查文件名是否匹配
    for tager in os.listdir(temp):
        #print(temp)
        if tager == target_name:
            # 构造完整文件路径
            t_source_path = os.path.join(temp, tager)
            # 构造新的文件名
            new_name = f"{counter}.png"
            destination_path = os.path.join(destination_folder, new_name)
            
            # 复制文件到目标文件夹并重命名
            shutil.copy2(t_source_path, destination_path)
            
            print(f"Copied and renamed: {tager} -> {new_name}")
            
            # 增加计数器
            counter += 1
