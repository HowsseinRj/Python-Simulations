# پیش‌بینی مصرف سوخت خودرو با استفاده از رگرسیون خطی
# نویسنده: Hossein Rajabloo

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# داده‌های فرضی مربوط به چند خودرو
data = {
    'Weight': [1000, 1200, 1400, 1600, 1800, 2000],
    'Horsepower': [70, 85, 95, 110, 125, 140],
    'Cylinders': [4, 4, 6, 6, 8, 8],
    'FuelEfficiency': [18, 17, 15, 13.5, 12, 11]  # mpg
}

df = pd.DataFrame(data)

# انتخاب ویژگی‌ها و هدف
X = df[['Weight', 'Horsepower', 'Cylinders']]
y = df['FuelEfficiency']

# مدل رگرسیون
model = LinearRegression()
model.fit(X, y)

# پیش‌بینی مقادیر
predictions = model.predict(X)

# رسم نمودار واقعی vs پیش‌بینی‌شده
plt.plot(y.values, label='Actual', marker='o')
plt.plot(predictions, label='Predicted', marker='x')
plt.title('پیش‌بینی مصرف سوخت خودرو')
plt.ylabel('مصرف سوخت (mpg)')
plt.xlabel('نمونه')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
