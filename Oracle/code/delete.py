import os
import shutil

def clear_single_folder(folder_path):
    """
    清空单个文件夹内的所有文件和子文件夹（保留文件夹本身）
    :param folder_path: 文件夹绝对路径
    """
    # 检查文件夹是否存在
    if not os.path.isdir(folder_path):
        print(f"文件夹不存在，跳过：{folder_path}")
        return

    # 遍历文件夹内所有内容
    for item in os.listdir(folder_path):
        # 拼接完整路径
        item_path = os.path.join(folder_path, item)
        
        try:
            # 如果是文件/符号链接，直接删除
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
                print(f"已删除文件：{item_path}")
            # 如果是文件夹，递归删除整个子文件夹
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"已删除子文件夹：{item_path}")
        except Exception as e:
            print(f"删除失败 {item_path}，原因：{str(e)}")


def clean_oracle_data():
    """
    主清理函数：执行所有清理任务
    """
    print("=" * 50)
    print("开始执行Oracle数据清理任务...")
    print("=" * 50)

    #需要清空的三个文件夹（保留文件夹，只删内容）
    target_folders = [
        r"../extracted_file",
        r"../graph",
        r"../nmon_csv"
    ]


    # 清空所有目标文件夹
    for folder in target_folders:
        print(f"正在清空文件夹：{folder}")
        clear_single_folder(folder)

    print("\n" + "=" * 50)
    print("Oracle数据清理任务执行完成！")
    print("=" * 50)

# 执行清理函数
if __name__ == "__main__":
    clean_oracle_data()