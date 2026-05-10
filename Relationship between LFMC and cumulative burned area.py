import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_excel(r'C:/Users/A/Desktop/LFMC-Burned area.xlsx')

# 按组划分数据
sf_data = data[data['Group'] == 'SF']
lf_data = data[data['Group'] == 'MF']
vlf_data = data[data['Group'] == 'LF']

# 对各组数据进行排序
sf_sorted = sf_data.sort_values(by='LFMC').reset_index(drop=True)
lf_sorted = lf_data.sort_values(by='LFMC').reset_index(drop=True)
vlf_sorted = vlf_data.sort_values(by='LFMC').reset_index(drop=True)

# 计算 LFMC 的累计百分比作为横坐标
sf_lfmc_cdf = np.arange(1, len(sf_sorted) + 1) / len(sf_sorted) * 100
lf_lfmc_cdf = np.arange(1, len(lf_sorted) + 1) / len(lf_sorted) * 100
vlf_lfmc_cdf = np.arange(1, len(vlf_sorted) + 1) / len(vlf_sorted) * 100

# 计算火灾面积的累计百分比作为纵坐标（范围在 0 - 1.0）
sf_burned_area_cdf = np.cumsum(sf_sorted['Forest Burned Area']) / sf_sorted['Forest Burned Area'].sum()
lf_burned_area_cdf = np.cumsum(lf_sorted['Forest Burned Area']) / lf_sorted['Forest Burned Area'].sum()
vlf_burned_area_cdf = np.cumsum(vlf_sorted['Forest Burned Area']) / vlf_sorted['Forest Burned Area'].sum()

# 计算各分组在标准分位数的LFMC值
standard_quantiles = [0, 25, 50, 75, 100]
all_quantiles = sorted(set(standard_quantiles + additional_quantiles))

# 使用quantile方法计算分位数[6,7,9](@ref)
sf_quantile_values = sf_sorted['LFMC'].quantile([q/100 for q in all_quantiles])
lf_quantile_values = lf_sorted['LFMC'].quantile([q/100 for q in all_quantiles])
vlf_quantile_values = vlf_sorted['LFMC'].quantile([q/100 for q in all_quantiles])

# 打印结果
print("=== 各分组LFMC分位数统计 ===")
print("\nSF组LFMC分位数:")
for q in all_quantiles:
    value = sf_quantile_values[q/100]
    print(f"  {q}%分位数: {value:.2f}")

print("\nMF组LFMC分位数:")
for q in all_quantiles:
    value = lf_quantile_values[q/100]
    print(f"  {q}%分位数: {value:.2f}")

print("\nLF组LFMC分位数:")
for q in all_quantiles:
    value = vlf_quantile_values[q/100]
    print(f"  {q}%分位数: {value:.2f}")

# 创建分位数结果表格
quantile_df = pd.DataFrame({
    'Quantile': all_quantiles,
    'SF_LFMC': [sf_quantile_values[q/100] for q in all_quantiles],
    'MF_LFMC': [lf_quantile_values[q/100] for q in all_quantiles],
    'LF_LFMC': [vlf_quantile_values[q/100] for q in all_quantiles]
})

# 创建35-45分位数详细表格
range_quantile_df = pd.DataFrame({
    'Quantile': quantile_range,
    'SF_LFMC': [sf_range_values[q/100] for q in quantile_range],
    'MF_LFMC': [lf_range_values[q/100] for q in quantile_range],
    'LF_LFMC': [vlf_range_values[q/100] for q in quantile_range]
})

print("\n=== 分位数汇总表 ===")
print(quantile_df)

# 保存分位数结果到CSV文件
quantile_df.to_csv('LFMC_quantile_results.csv', index=False)
print("\n分位数结果已保存到 'LFMC_quantile_results.csv'")

# 绘制 CDF
plt.figure(figsize=(8, 8))

# 绘制曲线
plt.plot(sf_lfmc_cdf, sf_burned_area_cdf, label='SF', color='black')
plt.plot(lf_lfmc_cdf, lf_burned_area_cdf, label='MF', color='orange')
plt.plot(vlf_lfmc_cdf, vlf_burned_area_cdf, label='LF', color='blue')

# 在图上标记关键分位数点（修复索引错误）
def mark_quantile_points(x_data, y_data, quantiles, color, label_prefix):
    """标记分位数点"""
    for q in quantiles:
        if q <= max(x_data):  # 确保分位数在数据范围内
            # 找到最接近分位数的数据点[8](@ref)
            closest_idx = np.argmin(np.abs(x_data - q))
            if closest_idx < len(y_data):  # 确保索引不越界
                x_pos = x_data[closest_idx]
                y_pos = y_data[closest_idx]
                plt.scatter(x_pos, y_pos, color=color, s=50, zorder=5)
                plt.annotate(f'{label_prefix} {q}%', (x_pos, y_pos), 
                           xytext=(10, 10), textcoords='offset points', 
                           fontsize=10, color=color)

# 标记各分组的关键点
mark_quantile_points(sf_lfmc_cdf, sf_burned_area_cdf, [25, 50, 75], 'black', 'SF')
mark_quantile_points(lf_lfmc_cdf, lf_burned_area_cdf, [25, 50, 75], 'orange', 'MF')
mark_quantile_points(vlf_lfmc_cdf, vlf_burned_area_cdf, [25, 35, 45, 50, 75], 'blue', 'LF')

# 图例和标签设置
plt.xlabel('LFMC quantile (%)', fontsize=22)
plt.ylabel('Cumulative fraction of SF, MF, LF', fontsize=22)
plt.title('LFMC quantile vs Cumulative fraction of Forest Burned Area', fontsize=18)
plt.legend(loc='lower right', fontsize=22)

# 设置网格线（包括在 25, 50, 75 处的内部虚线）
plt.grid(visible=True, linestyle='--', which='both')
plt.xticks(np.arange(0, 101, 25), fontsize=14)
plt.yticks(np.arange(0.0, 1.1, 0.25), fontsize=14)

# 显示图形
plt.tight_layout()
plt.show()


