





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('Energy_consumption.csv')

print(data.isnull().sum())

data.fillna(method='ffill', inplace=True)

scaler = StandardScaler()
data[['Temperature', 'Humidity']] =scaler.fit_transform(data[['Temperature', 'Humidity']])

sns.pairplot(data, diag_kind='kde')
plt.show()



from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

X = data[['Temperature', 'Humidity', 'Occupancy']]
y = data['EnergyConsumption']
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42)

model = Ridge()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)



import streamlit as st
import numpy as np
st.title("ENERGY CONSUMPTION PREDICTION")

temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
occupancy = st.radio("Occupancy", (0, 1))

if st.button("Predict"):
  input_features = np.array([[temperature, humidity, occupancy]])
  prediction = model.predict(input_features)[0]
  st.write(f"Predicted Energy Consumption: {prediction:.2f} kWh")



import joblib
joblib.dump(model, 'ridge_model.pkl')
