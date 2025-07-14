# پروژه پیشرفته پیش‌بینی مصرف سوخت با داده واقعی و مقایسه مدل‌ها
# نویسنده: Hossein Rajabloo

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# بارگذاری داده واقعی از اینترنت
url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/autos-mpg.csv"
df = pd.read_csv(url)

# حذف داده‌های ناقص
df.dropna(inplace=True)

# تبدیل ویژگی‌های غیرعددی
df = pd.get_dummies(df, columns=['origin'], drop_first=True)

# ورودی و خروجی
X = df.drop(['mpg', 'car name'], axis=1)
y = df['mpg']

# تقسیم به داده آموزش و تست
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# مدل ۱: رگرسیون خطی
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
pred_lr = model_lr.predict(X_test)

# مدل ۲: جنگل تصادفی (مدل هوشمندتر)
model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
model_rf.fit(X_train, y_train)
pred_rf = model_rf.predict(X_test)

# مقایسه عملکرد مدل‌ها
print("🔹 Linear Regression R²:", round(r2_score(y_test, pred_lr), 3))
print("🔹 Random Forest R²:", round(r2_score(y_test, pred_rf), 3))
print("🔹 Linear MAE:", round(mean_absolute_error(y_test, pred_lr), 2))
print("🔹 Random Forest MAE:", round(mean_absolute_error(y_test, pred_rf), 2))

# رسم نمودار مقایسه‌ای
plt.figure(figsize=(8, 5))
plt.plot(y_test.values[:30], label='Actual MPG', marker='o')
plt.plot(pred_lr[:30], label='Linear Predicted', marker='x')
plt.plot(pred_rf[:30], label='RF Predicted', marker='s')
plt.title('مقایسه پیش‌بینی مصرف سوخت - مدل‌های مختلف')
plt.ylabel('MPG')
plt.xlabel('نمونه‌ها')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
