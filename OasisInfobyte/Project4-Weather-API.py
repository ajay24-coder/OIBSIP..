import requests

# API endpoint and API key
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = "e3fcae19a097fc6faeb5c9e83fc99262"
#upload your own API key

def get_weather(location):
    try:
        # Construct API request
        params = {
            "q": location,
            "appid": api_key,
            "units": "metric"  # Use metric units (Celsius, km/h)
        }

        # Send request and get response
        response = requests.get(api_endpoint, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON response
            weather_data = response.json()

            # Extract relevant data
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            weather_condition = weather_data["weather"][0]["description"]

            # Print weather data
            print(f"Weather in {location}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {weather_condition}")
        else:
            print(f"Error: Failed to retrieve weather data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")

def main():
    while True:
        location = input("Enter city or ZIP code (or 'q' to quit): ")
        if location.lower() == 'q':
            break
        get_weather(location)

if __name__ == "__main__":
    main()