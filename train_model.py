import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# داده‌ها از اینترنت
url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/autos-mpg.csv"
df = pd.read_csv(url)
df.dropna(inplace=True)
df = pd.get_dummies(df, columns=['origin'], drop_first=True)

X = df.drop(['mpg', 'car name'], axis=1)
y = df['mpg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ذخیره مدل
joblib.dump((model, X.columns), 'fuel_model.pkl')
print("✅ مدل ذخیره شد.")
