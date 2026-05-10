import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import OLSInfluence

# 读取数据
file_path = 'C:/Users/A/Desktop/残差分析.xlsx'
data = pd.read_excel(file_path)

# 假设第一列是预测值，第二列是实测值
predicted = data.iloc[:, 0].values
observed = data.iloc[:, 1].values

# 计算普通残差
residuals = observed - predicted

# 将残差对实测值进行回归
X = sm.add_constant(observed)
model = sm.OLS(residuals, X).fit()

# 获取回归诊断中的标准化残差
ols_influence = OLSInfluence(model)
studentized_residuals = ols_influence.resid_studentized

# 创建图形
fig = plt.figure(figsize=(20, 8))

# 1. 直方图
ax1 = plt.subplot(1, 2, 1)

# 设置分箱
bin_edges = np.arange(-3, 3.5, 0.5)
n, bins, patches = ax1.hist(studentized_residuals, bins=bin_edges,
                           color='blue', edgecolor='black', 
                           alpha=0.7, density=False)

# 添加理论正态分布曲线
bin_centers = 0.5 * (bins[1:] + bins[:-1])
bin_width = bins[1] - bins[0]
pdf = stats.norm.pdf(bin_centers, 0, 1)
expected_freq = pdf * len(studentized_residuals) * bin_width
ax1.plot(bin_centers, expected_freq, 'k-', linewidth=2)

# 移除网格线
ax1.grid(False)

# 添加0竖线 [1,2](@ref)
ax1.axvline(x=0, color='black', linestyle='', linewidth=1.5)

# 设置坐标轴范围和刻度 - 用户可自定义
# 横坐标范围
ax1.set_xlim(-2.8, 3.2)
# 纵坐标范围
ax1.set_ylim(0, 10.6)

# 设置刻度 - 用户可自定义
# 横坐标刻度
ax1.set_xticks([-3, -2, -1, 0, 1, 2, 3])
# 纵坐标刻度
ax1.set_yticks(np.arange(0, 10.6, 2))

# 设置刻度标签字体大小 - 用户可自定义
ax1.tick_params(axis='both', which='major', labelsize=29)

# 移除标签
ax1.set_xlabel('Studentized Residual', fontsize=40)
ax1.set_ylabel('Frequency', fontsize=40)
ax1.set_title('')

# 2. 残差 vs 预测值散点图
ax2 = plt.subplot(1, 2, 2)

# 创建散点图
scatter = ax2.scatter(predicted, residuals, 
                      color='blue',
                      cmap='blue',
                      alpha=0.7,
                      edgecolors='black',
                      linewidth=0.5,
                      s=60,
                      vmin=-3, vmax=3)

# 移除网格线
ax2.grid(False)

# 添加0横线 [2,6](@ref)
ax2.axhline(y=0, color='black', linestyle='--', linewidth=1.5)

# 设置坐标轴范围和刻度 - 用户可自定义
# 横坐标范围（根据预测值范围调整）
ax2.set_xlim(predicted.min() - 20, predicted.max() + 12)
# 纵坐标范围（根据残差范围调整）
ax2.set_ylim(residuals.min() - 17, residuals.max() + 12)

# 横坐标刻度
ax2.set_xticks([90,100, 110, 120, 130, 140, 150, 160,170])
# 纵坐标刻度
ax2.set_yticks([-30, -20, -10, 0, 10, 20, 30])

# 设置刻度标签字体大小 - 用户可自定义
ax2.tick_params(axis='both', which='major', labelsize=29)

# 移除标签
ax2.set_xlabel('Predicted LFMC', fontsize=40)
ax2.set_ylabel('Residuals', fontsize=40)
ax2.set_title('')



plt.tight_layout()
plt.show()

# 输出统计信息
print(f"样本量: {len(studentized_residuals)}")
print(f"标准化残差均值: {studentized_residuals.mean():.3f}")
print(f"标准化残差标准差: {studentized_residuals.std():.3f}")
