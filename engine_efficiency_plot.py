# محاسبه و رسم نمودار راندمان موتور بر اساس درصد بار
# نویسنده: Hossein Rajabloo - پروژه آموزشی برای تحلیل عملکرد موتور

import numpy as np
import matplotlib.pyplot as plt

# مقادیر فرضی برای بار موتور (بر حسب درصد ظرفیت)
load_levels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# توان ورودی در هر سطح بار (kW)
input_kw = [5.2, 7.4, 10.1, 12.9, 15.0, 17.7, 20.5, 23.2, 25.6, 28.0]

# توان خروجی متناظر (kW)
output_kw = [2.3, 4.0, 6.2, 8.7, 10.9, 13.5, 15.9, 18.1, 20.4, 22.7]

# محاسبه راندمان برای هر سطح بار
efficiency_percent = []
for i in range(len(load_levels)):
    eta = (output_kw[i] / input_kw[i]) * 100
    efficiency_percent.append(round(eta, 1))  # گرد کردن به یک رقم اعشار

# رسم نمودار راندمان
plt.figure(figsize=(8, 5))
plt.plot(load_levels, efficiency_percent, marker='o', linestyle='-', color='darkorange')
plt.title('راندمان موتور در سطوح مختلف بار', fontsize=14)
plt.xlabel('بار موتور (% ظرفیت)', fontsize=12)
plt.ylabel('راندمان (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(load_levels)
plt.tight_layout()
plt.show()
