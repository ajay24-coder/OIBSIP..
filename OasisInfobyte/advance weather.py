#python
import tkinter as tk
import requests


def get_weather():
    city = location_entry.get()
    api_key = "18cb501f79313cd9ca44acae083a55b0"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&rapid={api_key}"
    response = requests.get(url)
    data = response.json()

    # Extract and display relevant weather information from the data
    # You can customize this part to show current conditions, forecasts, etc.


# Create the main application window
root = tk.Tk()
root.title("Weather App")

# Create a label and entry field for the location
location_label = tk.Label(root, text="Enter City:")
location_label.pack()

location_entry = tk.Entry(root)
location_entry.pack()

# Create a button to trigger weather data retrieval
search_button = tk.Button(root, text="Search", command=get_weather)
search_button.pack()

root.mainloop()
