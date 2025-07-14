# تحلیل ساده کاهش دما در لوله با استفاده از قانون سرمایش نیوتن
# نویسنده: Hossein Rajabloo

import numpy as np
import matplotlib.pyplot as plt

# پارامترهای اولیه
T_start = 90         # دمای اولیه مایع (°C)
T_env = 25           # دمای محیط (°C)
h = 15               # ضریب انتقال حرارت (W/m²·K)
area = 0.3           # سطح تماس لوله با هوا (m²)
mass = 2.5           # جرم آب (kg)
cp = 4180            # گرمای ویژه آب (J/kg·K)
duration = 1800      # زمان شبیه‌سازی (ثانیه)

# زمان‌ها به صورت آرایه
time = np.linspace(0, duration, 200)

# ضریب کلی انتقال حرارت
k = (h * area) / (mass * cp)

# دما در طول زمان (مدل نمایی)
temperature = T_env + (T_start - T_env) * np.exp(-k * time)

# رسم نمودار
plt.figure(figsize=(8, 5))
plt.plot(time / 60, temperature, color='darkblue')
plt.xlabel('زمان (دقیقه)')
plt.ylabel('دمای سیال (°C)')
plt.title('تحلیل کاهش دمای سیال در لوله در گذر زمان')
plt.grid(True)
plt.tight_layout()
plt.show()
