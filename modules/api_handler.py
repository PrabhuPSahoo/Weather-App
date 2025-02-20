import requests
from config import API_KEY, BASE_URL

# Function to get weather data
def get_weather_data(city: str):
    try:
        # Make the API request
        response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
        response.raise_for_status()  # Will raise an HTTPError if the response code is 4xx or 5xx
        
        # If the city is invalid, the API will return a "404" error status with a specific message
        data = response.json()
        if data.get("cod") != 200:  # Check if the "cod" field in the response is not 200 (OK)
            return None  # Return None if city is invalid
        
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
