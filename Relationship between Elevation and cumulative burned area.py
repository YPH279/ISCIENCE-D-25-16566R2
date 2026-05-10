import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 读取数据
df_data = pd.read_excel('C:/Users/A/Desktop/location.xlsx')

# 将 slope 和 FBA 提取为 X 和 y
X = df_data['elevation'].values.reshape(-1, 1)
y = df_data['FBA'].values

# 确定三个分段点
split_point1 = 2250  # 第一个分段点
split_point2 = 3000  # 第二个分段点
split_point3 = 3120  # 第三个分段点

# 分段数据
X_segment1 = X[X.flatten() <= split_point1]  # 第一段数据
y_segment1 = y[X.flatten() <= split_point1]

X_segment2 = X[(X.flatten() > split_point1) & (X.flatten() <= split_point2)]  # 第二段数据
y_segment2 = y[(X.flatten() > split_point1) & (X.flatten() <= split_point2)]

X_segment3 = X[(X.flatten() > split_point2) & (X.flatten() <= split_point3)]  # 第三段数据
y_segment3 = y[(X.flatten() > split_point2) & (X.flatten() <= split_point3)]

X_segment4 = X[X.flatten() > split_point3]  # 第四段数据
y_segment4 = y[X.flatten() > split_point3]

# 创建四个线性回归模型
model1 = LinearRegression().fit(X_segment1, y_segment1)
model2 = LinearRegression().fit(X_segment2, y_segment2)
model3 = LinearRegression().fit(X_segment3, y_segment3)
model4 = LinearRegression().fit(X_segment4, y_segment4)

# 生成预测数据
x_pred1 = np.linspace(min(X_segment1), max(X_segment1), 100).reshape(-1, 1)
y_pred1 = model1.predict(x_pred1)

x_pred2 = np.linspace(min(X_segment2), max(X_segment2), 100).reshape(-1, 1)
y_pred2 = model2.predict(x_pred2)

x_pred3 = np.linspace(min(X_segment3), max(X_segment3), 100).reshape(-1, 1)
y_pred3 = model3.predict(x_pred3)

x_pred4 = np.linspace(min(X_segment4), max(X_segment4), 100).reshape(-1, 1)
y_pred4 = model4.predict(x_pred4)

# 获取线性回归的参数
slope1, intercept1 = model1.coef_[0], model1.intercept_
slope2, intercept2 = model2.coef_[0], model2.intercept_
slope3, intercept3 = model3.coef_[0], model3.intercept_
slope4, intercept4 = model4.coef_[0], model4.intercept_

print("=== 分段线性回归方程 ===")
print(f"第一段 (x ≤ {split_point1}): y = {slope1:.4f}x + {intercept1:.4f}")
print(f"第二段 ({split_point1} < x ≤ {split_point2}): y = {slope2:.4f}x + {intercept2:.4f}")
print(f"第三段 ({split_point2} < x ≤ {split_point3}): y = {slope3:.4f}x + {intercept3:.4f}")
print(f"第四段 (x > {split_point3}): y = {slope4:.4f}x + {intercept4:.4f}")

# 计算每个分段点的函数值（用于检查连续性）
y_at_split1_model1 = model1.predict([[split_point1]])[0]
y_at_split1_model2 = model2.predict([[split_point1]])[0]
y_at_split2_model2 = model2.predict([[split_point2]])[0]
y_at_split2_model3 = model3.predict([[split_point2]])[0]
y_at_split3_model3 = model3.predict([[split_point3]])[0]
y_at_split3_model4 = model4.predict([[split_point3]])[0]

print(f"\n=== 分段点处的函数值 ===")
print(f"在 x={split_point1}:")
print(f"  第一段模型预测: {y_at_split1_model1:.4f}")
print(f"  第二段模型预测: {y_at_split1_model2:.4f}")
print(f"  差值: {abs(y_at_split1_model1 - y_at_split1_model2):.4f}")

print(f"在 x={split_point2}:")
print(f"  第二段模型预测: {y_at_split2_model2:.4f}")
print(f"  第三段模型预测: {y_at_split2_model3:.4f}")
print(f"  差值: {abs(y_at_split2_model2 - y_at_split2_model3):.4f}")

print(f"在 x={split_point3}:")
print(f"  第三段模型预测: {y_at_split3_model3:.4f}")
print(f"  第四段模型预测: {y_at_split3_model4:.4f}")
print(f"  差值: {abs(y_at_split3_model3 - y_at_split3_model4):.4f}")

# 绘制图表
plt.figure(figsize=(9, 7.75))
plt.scatter(X, y, color='black', alpha=0.6, label='Data', s=50)

# 绘制四段拟合线
plt.plot(x_pred1, y_pred1, color='blue', linewidth=3, label=f'Segment 1: y={slope1:.4f}x+{intercept1:.4f}')
plt.plot(x_pred2, y_pred2, color='blue', linewidth=3, label=f'Segment 2: y={slope2:.4f}x+{intercept2:.4f}')
plt.plot(x_pred3, y_pred3, color='blue', linewidth=3, label=f'Segment 3: y={slope3:.4f}x+{intercept3:.4f}')
plt.plot(x_pred4, y_pred4, color='blue', linewidth=3, label=f'Segment 4: y={slope4:.4f}x+{intercept4:.4f}')

# 绘制分段竖线
plt.axvline(x=2285, color='grey', linewidth=4.5, linestyle='-', alpha=0.7)
plt.axvline(x=split_point2, color='grey', linewidth=2, linestyle='-', alpha=0.7)
plt.axvline(x=split_point3, color='grey', linewidth=2, linestyle='--', alpha=0.7)

# 在分段点处标记
plt.scatter([split_point1], [y_at_split1_model1], color='black', s=80, zorder=5, marker='o')
plt.scatter([split_point2], [y_at_split2_model2], color='black', s=80, zorder=5, marker='o')
plt.scatter([split_point3], [y_at_split3_model3], color='black', s=80, zorder=5, marker='o')

# 设置坐标范围
plt.xlim(1500, 4000)
plt.ylim(-2, max(y) * 1.05)

# 设置纵坐标刻度
plt.yticks([0, 50, 100, 150], fontsize=20)

# 添加标题和标签
plt.title('Three-Segment Linear Regression', fontsize=18, fontweight='bold')
plt.xlabel('Elevation (m)', fontsize=28)
plt.ylabel('Cumulative Burned Area (Km²)', fontsize=28)

# 调整横纵坐标的字体大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)





# 显示图形
plt.tight_layout()
plt.show()

# 保存拟合参数
fit_params = {
    'split_points': [split_point1, split_point2, split_point3],
    'segment1_equation': f'y = {slope1:.4f}x + {intercept1:.4f}',
    'segment2_equation': f'y = {slope2:.4f}x + {intercept2:.4f}',
    'segment3_equation': f'y = {slope3:.4f}x + {intercept3:.4f}',
    'segment4_equation': f'y = {slope4:.4f}x + {intercept4:.4f}',
    'slope1': slope1, 'intercept1': intercept1,
    'slope2': slope2, 'intercept2': intercept2,
    'slope3': slope3, 'intercept3': intercept3,
    'slope4': slope4, 'intercept4': intercept4
}

print("\n=== 拟合参数总结 ===")
for key, value in fit_params.items():
    print(f"{key}: {value}")

# 计算整体R²值（所有段的综合拟合优度）
from sklearn.metrics import r2_score

# 为所有数据点预测值
y_pred_all = np.zeros_like(y)
for i, x_val in enumerate(X.flatten()):
    if x_val <= split_point1:
        y_pred_all[i] = model1.predict([[x_val]])[0]
    elif x_val <= split_point2:
        y_pred_all[i] = model2.predict([[x_val]])[0]
    elif x_val <= split_point3:
        y_pred_all[i] = model3.predict([[x_val]])[0]
    else:
        y_pred_all[i] = model4.predict([[x_val]])[0]

r2 = r2_score(y, y_pred_all)
print(f"\n整体模型R²值: {r2:.4f}")
