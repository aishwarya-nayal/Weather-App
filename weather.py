import requests
import json

# Function to fetch weather data
def get_weather(city, api_key):
    # URL for the API request
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # If the response is successful, parse and print the data
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant information from the response
        city_name = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        # Print weather information
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Failed to retrieve data for {city}. Error code: {response.status_code}")

# Main function
def main():
    # Your OpenWeatherMap API key
    api_key = "87319a123aa800a5063967551660ed27" 
    
    # Get city name from user
    city = input("Enter the city name: ")
    
    # Fetch and display weather information
    get_weather(city, api_key)

# Run the program
if __name__ == "__main__":
    main()
