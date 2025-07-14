import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# بارگذاری مدل
model, features = joblib.load('fuel_model.pkl')

# تابع پیش‌بینی
def predict():
    try:
        weight = float(entry_weight.get())
        horsepower = float(entry_hp.get())
        cylinders = int(entry_cyl.get())
        origin_2 = 1 if var_origin.get() == 'Europe' else 0
        origin_3 = 1 if var_origin.get() == 'Japan' else 0

        # ساخت ورودی مدل
        x = np.array([[cylinders, displacement.get(), horsepower, weight, acceleration.get(), model_year.get(), origin_2, origin_3]])
        pred = model.predict(x)[0]
        result_label.config(text=f'🔍 پیش‌بینی مصرف سوخت: {pred:.2f} MPG')

    except Exception as e:
        messagebox.showerror("خطا", "ورودی‌ها را درست وارد کنید!")

# ساخت پنجره GUI
root = tk.Tk()
root.title("پیش‌بینی مصرف سوخت خودرو")

tk.Label(root, text="وزن (kg):").grid(row=0, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1)

tk.Label(root, text="اسب‌بخار:").grid(row=1, column=0)
entry_hp = tk.Entry(root)
entry_hp.grid(row=1, column=1)

tk.Label(root, text="تعداد سیلندر:").grid(row=2, column=0)
entry_cyl = tk.Entry(root)
entry_cyl.grid(row=2, column=1)

tk.Label(root, text="منطقه تولید:").grid(row=3, column=0)
var_origin = tk.StringVar(value='USA')
tk.OptionMenu(root, var_origin, 'USA', 'Europe', 'Japan').grid(row=3, column=1)

tk.Button(root, text="پیش‌بینی", command=predict, bg="green", fg="white").grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
