import requests
import json

def get_weather(location):
    # API endpoint URL for weather data
    url = f"https://api.weatherapi.com/v1/current.json?key=661b900f19ac4f5f871154050231506 &q={location}"

    try:
        # Send a GET request to the API
        response = requests.get(url)
        data = json.loads(response.text)

        # Check if the response contains the 'current' key
        if 'current' in data:
            # Extract relevant weather information
            temperature = data['current']['temp_c']
            condition = data['current']['condition']['text']

            # Return the weather information
            return f"The current temperature in {location} is {temperature}°C with {condition}."
        else:
            return "Unable to fetch weather data for the given location."

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the API request
        return "An error occurred while fetching the weather data."


# Chatbot interface
print("Welcome to the Weather Chatbot!")

while True:
    location = input("Please enter a location (or 'exit' to quit): ")

    if location.lower() == 'exit':
        print("Thank you for using the Weather Chatbot. Goodbye!")
        break

    weather_info = get_weather(location)

    print(weather_info)
