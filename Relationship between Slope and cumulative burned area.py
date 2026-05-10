import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 读取数据
df_data = pd.read_excel('C:/Users/A/Desktop/location.xlsx')

# 将 DFMC 和 FBA 提取为 X 和 y
X = df_data['slope'].values.reshape(-1, 1)
y = df_data['FBA'].values

# 确定分段点
split_point = 40  # 只有一个分段点

# 分段数据
X_pre_split = X[X.flatten() <= split_point]  # 分段点前的数据
y_pre_split = y[X.flatten() <= split_point]

X_post_split = X[X.flatten() > split_point]  # 分段点后的数据
y_post_split = y[X.flatten() > split_point]

# 分段点前：使用图中的幂函数公式 y = 0.5241 * x^2.7677
def power_function(x):
    """幂函数公式：y = 0.5241 * x^2.7677"""
    return 0.005241 * (x ** 2.7677)

# 为分段点前数据生成预测
x_pred_pre = np.linspace(min(X_pre_split), max(X_pre_split), 100).flatten()
y_pred_pre = power_function(x_pred_pre)

# 分段点后：使用线性回归
model_post = LinearRegression().fit(X_post_split, y_post_split)
x_pred_post = np.linspace(min(X_post_split), max(X_post_split), 100).reshape(-1, 1)
y_pred_post = model_post.predict(x_pred_post)

# 获取线性回归的参数
linear_slope = model_post.coef_[0]
linear_intercept = model_post.intercept_
print(f"分段点后线性回归方程: y = {linear_slope:.4f}x + {linear_intercept:.4f}")

# 计算分段点处的函数值，确保曲线平滑连接
# 计算幂函数在分段点处的值
y_at_split_power = power_function(split_point)
# 计算线性回归在分段点处的值
y_at_split_linear = model_post.predict([[split_point]])[0]

print(f"分段点 x={split_point}:")
print(f"  幂函数值: {y_at_split_power:.4f}")
print(f"  线性回归值: {y_at_split_linear:.4f}")
print(f"  差值: {abs(y_at_split_power - y_at_split_linear):.4f}")

# 为了确保曲线平滑连接，我们将线性回归的截距调整为通过幂函数在分段点的值
adjusted_intercept = y_at_split_power - linear_slope * split_point
print(f"调整后的线性回归截距: {adjusted_intercept:.4f}")

# 使用调整后的线性回归方程
def adjusted_linear_function(x):
    """调整后的线性回归方程，确保在分段点处与幂函数连接"""
    return linear_slope * x + adjusted_intercept

y_pred_post_adjusted = adjusted_linear_function(x_pred_post)

# 绘制图表
plt.figure(figsize=(9, 7.75))
plt.scatter(X, y, color='black', alpha=0.6, label='Data')

# 绘制分段拟合曲线
# 分段点前：幂函数拟合
plt.plot(x_pred_pre, y_pred_pre, color='blue', linewidth=3, label='Power Fit (y=0.5241x^2.7677)')

# 分段点后：调整后的线性回归拟合
plt.plot(x_pred_post, y_pred_post_adjusted, color='blue', linewidth=3, label=f'Linear Fit (y={linear_slope:.4f}x+{adjusted_intercept:.4f})')

# 绘制分段竖线
plt.axvline(x=40, color='grey', linewidth=4, linestyle='-', alpha=0.7)

# 在分段点处标记
plt.scatter([split_point], [y_at_split_power], color='black', s=60, zorder=5, 
            label=f'Split Point (x={split_point})')

# 设置坐标范围
plt.xlim(0, 60)
plt.ylim(0, max(y) * 1.05)

# 设置纵坐标刻度为0, 50, 100, 150
plt.yticks([0, 50, 100, 150], fontsize=25)

# 添加标题和标签
plt.title('Segmented Fit: Power Function + Linear Regression', fontsize=16, fontweight='bold')
plt.xlabel('Slope(°)', fontsize=28)
plt.ylabel('Cumulative Burned Area (Km²)', fontsize=28)

# 调整横纵坐标的字体大小
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)



# 在图上显示公式
formula_text = f'Power: y = 0.005241x^{2.77}'
plt.text(0.05, 0.95, formula_text, transform=plt.gca().transAxes, 
         fontsize=20, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# 显示图形
plt.tight_layout()
plt.show()

# 保存拟合参数
fit_params = {
    'split_point': split_point,
    'power_function': 'y = 0.5241 * x^2.7677',
    'linear_slope': linear_slope,
    'linear_intercept': linear_intercept,
    'adjusted_intercept': adjusted_intercept,
    'adjusted_linear_function': f'y = {linear_slope:.4f}x + {adjusted_intercept:.4f}',
    'y_at_split_power': y_at_split_power,
    'y_at_split_linear': y_at_split_linear
}

print("\n拟合参数总结:")
for key, value in fit_params.items():
    print(f"{key}: {value}")
