import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os


def plot_cpu_utilization(csv_path, save_folder):
    """
    读取指定路径的 CPU CSV 文件并生成堆叠面积图保存到指定文件夹。
    
    参数:
    csv_path: str, CSV 文件的完整路径
    save_folder: str, 图片保存的文件夹路径
    """
    try:
        # 1. 确保保存目录存在
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
            print(f"创建目录: {save_folder}")

        # 2. 读取 CSV 文件
        df = pd.read_csv(csv_path)

        # 3. 处理数据
        # 获取第一列（时间列）并转换格式
        time_col = df.columns[0] 
        df[time_col] = pd.to_datetime(df[time_col])

        # 提取绘图数据
        time_data = df[time_col]
        user_data = df['User%']
        sys_data = df['Sys%']
        wait_data = df['Wait%']

        # 4. 绘图设置
        plt.figure(figsize=(12, 6))
        
        # 绘制堆叠面积图
        plt.stackplot(time_data, user_data, sys_data, wait_data, 
                      labels=['User', 'System', 'Wait'], 
                      colors=['#1f77b4', '#ff7f0e', '#2ca02c'], 
                      alpha=0.8)

        # 5. 图表修饰
        plt.title('cpu utilization', fontsize=16, fontweight='bold')
        plt.xlabel('Time', fontsize=12)
        plt.ylabel('Percentage (%)', fontsize=12)
        
        # 纵轴固定刻度
        plt.ylim(0, 100)
        plt.yticks([0, 20, 40, 60, 80, 100])

        # 横轴整点刻度设置
        ax = plt.gca()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        # 每 2 小时一个刻度，如果数据跨度小可以改为 1
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) 
        plt.xticks(rotation=0, ha='center')

        plt.legend(loc='upper left')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()

        # 6. 生成保存文件名
        # 使用原文件名（去掉扩展名）作为图片名
        file_name = os.path.splitext(os.path.basename(csv_path))[0]
        save_path = os.path.join(save_folder, f"{file_name}.png")

        # 7. 保存图片
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close() # 及时关闭画布，防止批量处理时内存溢出
        print(f"成功保存图表: {save_path}")

    except Exception as e:
        print(f"处理文件 {csv_path} 时出错: {e}")
 
 
 
 
        
def plot_memory_usage(csv_path, save_folder):
    """
    读取 MEM CSV 文件并生成内存堆叠面积图。
    绘制列：active, inactive, memfree
    """
    try:
        # 1. 确保目录存在
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # 2. 读取数据
        df = pd.read_csv(csv_path)

        # 3. 数据预处理
        time_col = df.columns[0]
        df[time_col] = pd.to_datetime(df[time_col])
        
        # 提取指定的内存列
        time_data = df[time_col]
        active = df['active']
        inactive = df['inactive']
        memfree = df['memfree']

        # 4. 开始绘图
        plt.figure(figsize=(12, 6))
        
        # 绘制堆叠面积图
        # 颜色选用：深蓝(Active), 浅蓝(Inactive), 绿色(Free)
        plt.stackplot(time_data, active, inactive, memfree, 
                      labels=['Active', 'Inactive', 'MemFree'], 
                      colors=['#1f77b4', '#aec7e8', '#2ca02c'], 
                      alpha=0.8)

        # 5. 图表修饰
        plt.title('Memory Usage', fontsize=16, fontweight='bold')
        plt.xlabel('Time', fontsize=12)
        plt.ylabel('Memory (MB)', fontsize=12)

        # 横轴设置：整点显示，不旋转
        ax = plt.gca()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) 
        plt.xticks(rotation=0, ha='center')

        # 纵轴设置：让 Y 轴从 0 开始，最大值自动适应并留出一点空间
        plt.ylim(0, (active + inactive + memfree).max() * 1.1)

        plt.legend(loc='upper left')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()

        # 6. 保存图片
        file_name = os.path.splitext(os.path.basename(csv_path))[0]
        save_path = os.path.join(save_folder, f"{file_name}_memory.png")
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"内存图表已保存至: {save_path}")

    except Exception as e:
        print(f"处理内存文件 {csv_path} 时出错: {e}")


def plot_hugepages_raw(csv_path, save_folder):
    """
    读取 HUGEPAGES CSV 文件并生成多系列折线图。
    纵轴直接显示 CSV 中的原始数值，不进行单位转换。
    """
    try:
        # 1. 确保目录存在
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # 2. 读取数据
        df = pd.read_csv(csv_path)

        # 3. 数据处理
        time_col = df.columns[0]
        df[time_col] = pd.to_datetime(df[time_col])
        
        time_data = df[time_col]
        huge_total = df['HugeTotal']
        huge_free = df['HugeFree']
        huge_size = df['HugeSizeMB']

        # 4. 开始绘图
        plt.figure(figsize=(12, 6))
        
        # 绘制折线图
        plt.plot(time_data, huge_total, label='HugeTotal', color='#d62728', linewidth=2)
        plt.plot(time_data, huge_free, label='HugeFree', color='#2ca02c', linewidth=2)
        plt.plot(time_data, huge_size, label='HugeSizeMB', color='#7f7f7f', linestyle='--')

        # 5. 图表修饰
        plt.title('HUGEPAGES', fontsize=16, fontweight='bold')
        plt.xlabel('Time', fontsize=12)
        plt.ylabel('Value', fontsize=12)  # 纵轴只标注为 Value

        # 横轴设置：整点显示，不旋转
        ax = plt.gca()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) 
        plt.xticks(rotation=0, ha='center')

        # 纵轴设置：从 0 开始，自动适应最大值
        plt.ylim(0, huge_total.max() * 1.1)

        plt.legend(loc='upper right')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()

        # 6. 保存图片
        file_name = os.path.splitext(os.path.basename(csv_path))[0]
        save_path = os.path.join(save_folder, f"{file_name}_hugepages.png")
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"图表已保存至: {save_path}")

    except Exception as e:
        print(f"处理文件时出错: {e}")
        

def plot_network_io(csv_path, save_folder, resample_rule='5T'):
    """
    读取 NET CSV 文件并生成网络 I/O 多系列时间序列折线图。
    - 所有折线均为实线。
    - 在采样位置显示标记点。
    - 允许手动调整标记点的密度 (markevery)。

    参数:
    - csv_path: CSV 文件路径
    - save_folder: 图片保存目录
    - resample_rule: 采样频率字符串 (默认 '5T')
    """
    try:
        # 1. 确保目录存在
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # 2. 读取数据
        df = pd.read_csv(csv_path)

        # 3. 数据预处理
        time_col = df.columns[0]
        df[time_col] = pd.to_datetime(df[time_col])
        
        # 将时间设为索引
        df.set_index(time_col, inplace=True)
        
        # --- 采样部分 (保留) ---
        # 重采样并插值
        df_resampled = df.resample(resample_rule).mean().interpolate(method='linear')
        
        time_data = df_resampled.index
        pub_read = df_resampled['public-read-KB/s']
        pri_read = df_resampled['private-read-KB/s']
        pub_write = df_resampled['public-write-KB/s']
        pri_write = df_resampled['private-write-KB/s']

        # 4. 开始绘图
        plt.figure(figsize=(12, 6))
        
        # 定义采样点的标记样式
        # marker='o' 表示圆形标记
        # markersize=4 标记大小
        # markevery=2 表示每 2 个重采样点显示一个标记
        marker_style = {'marker': 'o', 'markersize': 4, 'markevery': 1}
        
        # 绘制折线图：全部改为实线 (linestyle='-')，加入采样点标记
        plt.plot(time_data, pub_read, label='Public Read', color='#1f77b4', linewidth=1.5, linestyle='-', **marker_style)
        plt.plot(time_data, pri_read, label='Private Read', color='#2ca02c', linewidth=1.5, linestyle='-', **marker_style)
        plt.plot(time_data, pub_write, label='Public Write', color='#ff7f0e', linewidth=1.5, linestyle='-', **marker_style)
        plt.plot(time_data, pri_write, label='Private Write', color='#d62728', linewidth=1.5, linestyle='-', **marker_style)

        # 5. 图表修饰
        plt.title('NET', fontsize=16, fontweight='bold')
        plt.xlabel('Time', fontsize=12)
        plt.ylabel('KB/s', fontsize=12)

        # 横轴设置
        ax = plt.gca()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator()) 
        plt.xticks(rotation=0, ha='center')

        # 纵轴设置
        max_val = df_resampled[['public-read-KB/s', 'private-read-KB/s', 'public-write-KB/s', 'private-write-KB/s']].max().max()
        plt.ylim(0, max_val * 1.15) 

        # 图例：也显示标记
        plt.legend(loc='upper right', fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()

        # 6. 保存图片
        file_name = os.path.splitext(os.path.basename(csv_path))[0]
        save_path = os.path.join(save_folder, "nets.png") # 文件名略作修改，避免覆盖
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"网络 I/O 图表已保存至: {save_path} (频率: {resample_rule})")

    except Exception as e:
        print(f"处理网络文件 {csv_path} 时出错: {e}")
        

def csv_to_graph(cpu_csv,mem_csv,hugepages_csv,net_csv,output_dir):

    plot_cpu_utilization(cpu_csv, output_dir)
    plot_memory_usage(mem_csv, output_dir)
    plot_hugepages_raw(hugepages_csv, output_dir)
    plot_network_io(net_csv, output_dir,'12min')

if __name__ == "__main__":
        # --- 使用示例 ---
    cpu_csv = r'G:\project_zhou\data\Oracle\nmon_output1\csv\CPU_ALL.csv'
    mem_csv = r'G:\project_zhou\data\Oracle\nmon_output1\csv\MEM.csv'
    hugepages_csv = r'G:\project_zhou\data\Oracle\nmon_output1\csv\HUGEPAGES.csv'
    net_csv = r'G:\project_zhou\data\Oracle\nmon_output1\csv\NET.csv'
    output_dir = r'G:\project_zhou\data\Oracle\out_picture'
    
    csv_to_graph(cpu_csv,mem_csv,hugepages_csv,net_csv,output_dir)
