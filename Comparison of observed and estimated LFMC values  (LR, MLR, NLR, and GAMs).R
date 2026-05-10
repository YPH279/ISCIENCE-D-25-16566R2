######哨兵提取校正点和建模点##########
library(ggplot2)
library(dplyr)

# 输入数据
setwd("C:/Users/A/Desktop") # 设置工作目录
data = read.csv("s2.csv") # 读取数据

# 随机选择校正点
calibration_df <- data %>% sample_frac(1/3, replace = FALSE, seed = 999)
# 剩余数据作为建模点
modeling_df <- data[!(data$MLR %in% calibration_df$MLR), ]


# 分别对MLR和NLR的校正数据集进行线性回归分析并计算R方
calibration_mlr_model <- lm(LFMC ~ MLR, data = calibration_df)
calibration_nlr_model <- lm(LFMC ~ NLR, data = calibration_df)
calibration_gam_model <- lm(LFMC ~ GAM, data = calibration_df)
calibration_mlr_r2 <- summary(calibration_mlr_model)$r.squared
calibration_nlr_r2 <- summary(calibration_nlr_model)$r.squared
calibration_gam_r2 <- summary(calibration_gam_model)$r.squared

# 分别对MLR和NLR的建模数据集进行线性回归分析并计算R方
modeling_mlr_model <- lm(LFMC ~ MLR, data = modeling_df)
modeling_nlr_model <- lm(LFMC ~ NLR, data = modeling_df)
modeling_gam_model <- lm(LFMC ~ GAM, data = modeling_df)
modeling_mlr_r2 <- summary(modeling_mlr_model)$r.squared
modeling_nlr_r2 <- summary(modeling_nlr_model)$r.squared
modeling_gam_r2 <- summary(modeling_gam_model)$r.squared

# 创建一个包含两个图的列表
plots_list <- list()

# MLR图
plots_list[['MLR']] <- ggplot(data, aes(x = MLR, y = LFMC)) +
  geom_point(aes(color = 'All Data'), alpha = 0.3) +
  geom_point(data = calibration_df, aes(color = 'Calibration'), size = 3) +
  geom_point(data = modeling_df, aes(color = 'Modeling'), size = 3) +
  geom_smooth(data = modeling_df, method = "lm", se = FALSE, formula = y ~ x, color = 'blue') +
  geom_smooth(data = calibration_df, method = "lm", se = FALSE, formula = y ~ x, color = 'red') +
  labs(title = "MLR vs LFMC", subtitle = paste0("R² Calibration = ", round(calibration_mlr_r2, 2), 
                                                ", R² Modeling = ", round(modeling_mlr_r2, 2))) +
  scale_color_manual(values = c('All Data' = 'black', 'Calibration' = 'red', 'Modeling' = 'blue'))

# NLR图
plots_list[['NLR']] <- ggplot(data, aes(x = NLR, y = LFMC)) +
  geom_point(aes(color = 'All Data'), alpha = 0.3) +
  geom_point(data = calibration_df, aes(color = 'Calibration'), size = 3) +
  geom_point(data = modeling_df, aes(color = 'Modeling'), size = 3) +
  geom_smooth(data = modeling_df, method = "lm", se = FALSE, formula = y ~ x, color = 'blue') +
  geom_smooth(data = calibration_df, method = "lm", se = FALSE, formula = y ~ x, color = 'red') +
  labs(title = "NLR vs LFMC", subtitle = paste0("R² Calibration = ", round(calibration_nlr_r2, 2), 
                                                ", R² Modeling = ", round(modeling_nlr_r2, 2))) +
  scale_color_manual(values = c('All Data' = 'black', 'Calibration' = 'red', 'Modeling' = 'blue'))


# GAM图
plots_list[['GAM']] <- ggplot(data, aes(x = GAM, y = LFMC)) +
  geom_point(aes(color = 'All Data'), alpha = 0.3) +
  geom_point(data = calibration_df, aes(color = 'Calibration'), size = 3) +
  geom_point(data = modeling_df, aes(color = 'Modeling'), size = 3) +
  geom_smooth(data = modeling_df, method = "lm", se = FALSE, formula = y ~ x, color = 'blue') +
  geom_smooth(data = calibration_df, method = "lm", se = FALSE, formula = y ~ x, color = 'red') +
  labs(title = "GAM vs LFMC", subtitle = paste0("R² Calibration = ", round(calibration_gam_r2, 2), 
                                                ", R² Modeling = ", round(modeling_gam_r2, 2))) +
  scale_color_manual(values = c('All Data' = 'black', 'Calibration' = 'red', 'Modeling' = 'blue'))


# 输出图形
print(plots_list[['MLR']])
print(plots_list[['NLR']])
print(plots_list[['GAM']])



# 输出用于建模和校正的数据
cat("Calibration data:\n")
print(calibration_df)
cat("\n")
cat("Modeling data:\n")
print(modeling_df)




######MOD09GA提取校正点和建模点##########
library(ggplot2)
library(dplyr)

# 输入数据
setwd("C:/Users/A/Desktop") # 设置工作目录
data = read.csv("M09.csv") # 读取数据

# 随机选择校正点
calibration_df <- data %>% sample_frac(1/3, replace = FALSE, seed = 999)
# 剩余数据作为建模点
modeling_df <- data[!(data$MLR %in% calibration_df$MLR), ]


# 分别对MLR和NLR的校正数据集进行线性回归分析并计算R方
calibration_mlr_model <- lm(LFMC ~ MLR, data = calibration_df)
calibration_nlr_model <- lm(LFMC ~ NLR, data = calibration_df)
calibration_gam_model <- lm(LFMC ~ GAM, data = calibration_df)
calibration_mlr_r2 <- summary(calibration_mlr_model)$r.squared
calibration_nlr_r2 <- summary(calibration_nlr_model)$r.squared
calibration_gam_r2 <- summary(calibration_gam_model)$r.squared

# 分别对MLR和NLR的建模数据集进行线性回归分析并计算R方
modeling_mlr_model <- lm(LFMC ~ MLR, data = modeling_df)
modeling_nlr_model <- lm(LFMC ~ NLR, data = modeling_df)
modeling_gam_model <- lm(LFMC ~ GAM, data = modeling_df)
modeling_mlr_r2 <- summary(modeling_mlr_model)$r.squared
modeling_nlr_r2 <- summary(modeling_nlr_model)$r.squared
modeling_gam_r2 <- summary(modeling_gam_model)$r.squared

# 创建一个包含两个图的列表
plots_list <- list()

# MLR图
plots_list[['MLR']] <- ggplot(data, aes(x = MLR, y = LFMC)) +
  geom_point(aes(color = 'All Data'), alpha = 0.3) +
  geom_point(data = calibration_df, aes(color = 'Calibration'), size = 3) +
  geom_point(data = modeling_df, aes(color = 'Modeling'), size = 3) +
  geom_smooth(data = modeling_df, method = "lm", se = FALSE, formula = y ~ x, color = 'blue') +
  geom_smooth(data = calibration_df, method = "lm", se = FALSE, formula = y ~ x, color = 'red') +
  labs(title = "MLR vs LFMC", subtitle = paste0("R² Calibration = ", round(calibration_mlr_r2, 2), 
                                                ", R² Modeling = ", round(modeling_mlr_r2, 2))) +
  scale_color_manual(values = c('All Data' = 'black', 'Calibration' = 'red', 'Modeling' = 'blue'))

# NLR图
plots_list[['NLR']] <- ggplot(data, aes(x = NLR, y = LFMC)) +
  geom_point(aes(color = 'All Data'), alpha = 0.3) +
  geom_point(data = calibration_df, aes(color = 'Calibration'), size = 3) +
  geom_point(data = modeling_df, aes(color = 'Modeling'), size = 3) +
  geom_smooth(data = modeling_df, method = "lm", se = FALSE, formula = y ~ x, color = 'blue') +
  geom_smooth(data = calibration_df, method = "lm", se = FALSE, formula = y ~ x, color = 'red') +
  labs(title = "NLR vs LFMC", subtitle = paste0("R² Calibration = ", round(calibration_nlr_r2, 2), 
                                                ", R² Modeling = ", round(modeling_nlr_r2, 2))) +
  scale_color_manual(values = c('All Data' = 'black', 'Calibration' = 'red', 'Modeling' = 'blue'))


# GAM图
plots_list[['GAM']] <- ggplot(data, aes(x = GAM, y = LFMC)) +
  geom_point(aes(color = 'All Data'), alpha = 0.3) +
  geom_point(data = calibration_df, aes(color = 'Calibration'), size = 3) +
  geom_point(data = modeling_df, aes(color = 'Modeling'), size = 3) +
  geom_smooth(data = modeling_df, method = "lm", se = FALSE, formula = y ~ x, color = 'blue') +
  geom_smooth(data = calibration_df, method = "lm", se = FALSE, formula = y ~ x, color = 'red') +
  labs(title = "GAM vs LFMC", subtitle = paste0("R² Calibration = ", round(calibration_gam_r2, 2), 
                                                ", R² Modeling = ", round(modeling_gam_r2, 2))) +
  scale_color_manual(values = c('All Data' = 'black', 'Calibration' = 'red', 'Modeling' = 'blue'))


# 输出图形
print(plots_list[['MLR']])
print(plots_list[['NLR']])
print(plots_list[['GAM']])



# 输出用于建模和校正的数据
cat("Calibration data:\n")
print(calibration_df)
cat("\n")
cat("Modeling data:\n")
print(modeling_df)





install.packages("gridExtra")
library(gridExtra)

######MCD43A4提取校正点和建模点##########
library(ggplot2)
library(dplyr)

# 输入数据
setwd("C:/Users/A/Desktop") # 设置工作目录
data = read.csv("M43.csv") # 读取数据

# 随机选择校正点
calibration_df <- data %>% sample_frac(1/3, replace = FALSE, seed = 999)
# 剩余数据作为建模点
modeling_df <- data[!(data$MLR %in% calibration_df$MLR), ]


# 分别对MLR和NLR的校正数据集进行线性回归分析并计算R方
calibration_lr_model <- lm(LFMC ~ LR, data = calibration_df)
calibration_mlr_model <- lm(LFMC ~ MLR, data = calibration_df)
calibration_nlr_model <- lm(LFMC ~ NLR, data = calibration_df)
calibration_gam_model <- lm(LFMC ~ GAM, data = calibration_df)
calibration_lr_r2 <- summary(calibration_lr_model)$r.squared
calibration_mlr_r2 <- summary(calibration_mlr_model)$r.squared
calibration_nlr_r2 <- summary(calibration_nlr_model)$r.squared
calibration_gam_r2 <- summary(calibration_gam_model)$r.squared

# 分别对MLR和NLR的建模数据集进行线性回归分析并计算R方
modeling_lr_model <- lm(LFMC ~ LR, data = modeling_df)
modeling_mlr_model <- lm(LFMC ~ MLR, data = modeling_df)
modeling_nlr_model <- lm(LFMC ~ NLR, data = modeling_df)
modeling_gam_model <- lm(LFMC ~ GAM, data = modeling_df)
modeling_lr_r2 <- summary(modeling_lr_model)$r.squared
modeling_mlr_r2 <- summary(modeling_mlr_model)$r.squared
modeling_nlr_r2 <- summary(modeling_nlr_model)$r.squared
modeling_gam_r2 <- summary(modeling_gam_model)$r.squared

# 创建一个包含两个图的列表
plots_list <- list()

# LR图
plots_list[['LR']] <- ggplot(data, aes(x = LR, y = LFMC)) +
  geom_point(aes(color = 'All Data'), alpha = 0.3) +
  geom_point(data = calibration_df, aes(color = 'Calibration'), size = 3) +
  geom_point(data = modeling_df, aes(color = 'Modeling'), size = 3) +
  geom_smooth(data = modeling_df, method = "lm", se = FALSE, formula = y ~ x, color = 'blue') +
  geom_smooth(data = calibration_df, method = "lm", se = FALSE, formula = y ~ x, color = 'red') +
  labs(title = "LR vs LFMC", subtitle = paste0("R² Cal = ", round(calibration_lr_r2, 2), 
                                               ", R² Mod = ", round(modeling_mlr_r2, 2))) +
  scale_color_manual(values = c('All Data' = 'black', 'Calibration' = 'red', 'Modeling' = 'blue'))

# MLR图
plots_list[['MLR']] <- ggplot(data, aes(x = MLR, y = LFMC)) +
  geom_point(aes(color = 'All Data'), alpha = 0.3) +
  geom_point(data = calibration_df, aes(color = 'Calibration'), size = 3) +
  geom_point(data = modeling_df, aes(color = 'Modeling'), size = 3) +
  geom_smooth(data = modeling_df, method = "lm", se = FALSE, formula = y ~ x, color = 'blue') +
  geom_smooth(data = calibration_df, method = "lm", se = FALSE, formula = y ~ x, color = 'red') +
  labs(title = "MLR vs LFMC", subtitle = paste0("R² Cal = ", round(calibration_mlr_r2, 2), 
                                                ", R² Mod = ", round(modeling_mlr_r2, 2))) +
  scale_color_manual(values = c('All Data' = 'black', 'Calibration' = 'red', 'Modeling' = 'blue'))

# NLR图
plots_list[['NLR']] <- ggplot(data, aes(x = NLR, y = LFMC)) +
  geom_point(aes(color = 'All Data'), alpha = 0.3) +
  geom_point(data = calibration_df, aes(color = 'Calibration'), size = 3) +
  geom_point(data = modeling_df, aes(color = 'Modeling'), size = 3) +
  geom_smooth(data = modeling_df, method = "lm", se = FALSE, formula = y ~ x, color = 'blue') +
  geom_smooth(data = calibration_df, method = "lm", se = FALSE, formula = y ~ x, color = 'red') +
  labs(title = "NLR vs LFMC", subtitle = paste0("R² Cal = ", round(calibration_nlr_r2, 2), 
                                                ", R² Mod = ", round(modeling_nlr_r2, 2))) +
  scale_color_manual(values = c('All Data' = 'black', 'Calibration' = 'red', 'Modeling' = 'blue'))


# GAM图
plots_list[['GAM']] <- ggplot(data, aes(x = GAM, y = LFMC)) +
  geom_point(aes(color = 'All Data'), alpha = 0.3) +
  geom_point(data = calibration_df, aes(color = 'Calibration'), size = 3) +
  geom_point(data = modeling_df, aes(color = 'Modeling'), size = 3) +
  geom_smooth(data = modeling_df, method = "lm", se = FALSE, formula = y ~ x, color = 'blue') +
  geom_smooth(data = calibration_df, method = "lm", se = FALSE, formula = y ~ x, color = 'red') +
  labs(title = "GAM vs LFMC", subtitle = paste0("R² Cal = ", round(calibration_gam_r2, 2), 
                                                ", R² Mod = ", round(modeling_gam_r2, 2))) +
  scale_color_manual(values = c('All Data' = 'black', 'Calibration' = 'red', 'Modeling' = 'blue'))


# 输出图形
print(plots_list[['LR']])
print(plots_list[['MLR']])
print(plots_list[['NLR']])
print(plots_list[['GAM']])



library(gridExtra)

# 假设 plots_list 中的图形已经创建完毕
grid.arrange(plots_list[['LR']], plots_list[['MLR']], 
             plots_list[['NLR']], plots_list[['GAM']], 
             ncol = 2, nrow = 2)



# 输出用于建模和校正的数据
cat("Calibration data:\n")
print(calibration_df)
cat("\n")
cat("Modeling data:\n")
print(modeling_df)