import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# ------------------ CONFIGURATION ------------------
API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API Key
CITY = "London"  # Change city as needed
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# ------------------ FETCH DATA ------------------
response = requests.get(URL)
data = response.json()

dates = []
temps = []
humidity = []

for forecast in data["list"]:
    dt = datetime.datetime.fromtimestamp(forecast["dt"])
    dates.append(dt)
    temps.append(forecast["main"]["temp"])
    humidity.append(forecast["main"]["humidity"])

# ------------------ DATA VISUALIZATION ------------------
plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")

plt.subplot(2, 1, 1)
sns.lineplot(x=dates, y=temps, color="orange", marker="o")
plt.title(f"Temperature Forecast for {CITY}")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

plt.subplot(2, 1, 2)
sns.lineplot(x=dates, y=humidity, color="blue", marker="o")
plt.title(f"Humidity Forecast for {CITY}")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
