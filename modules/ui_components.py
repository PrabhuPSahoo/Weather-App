import streamlit as st
from modules.utils import convert_temperature


# Function to render weather form and collect user input
def weather_form():
    with st.form(key="weather_form"):
        city = st.text_input("Enter city name:")
        submit_button = st.form_submit_button(label="Get Weather")

    if submit_button or city:
        return city
    return None


def display_weather(data, temperature_celsius):
    # Extract weather information from the data
    weather_condition = data["weather"][0]["main"]
    wind_speed = data["wind"]["speed"]
    humidity = data["main"]["humidity"]
    
    # Define icons for weather conditions
    weather_icons = {
        "Clear": "☀️",  # Sun icon
        "Clouds": "☁️",  # Cloud icon
        "Rain": "🌧️",  # Rain icon
        "Snow": "❄️",  # Snowflake icon
        "Thunderstorm": "⚡",  # Lightning icon
        "Drizzle": "🌦️",  # Drizzle icon
    }
    
    # Get the corresponding weather icon or default to Earth if unknown
    weather_icon = weather_icons.get(weather_condition, "🌍")
    
    # Convert temperature to Celsius
    temperature = temperature_celsius

    # Display weather details
    st.markdown(f"### Current Weather: {weather_icon} {weather_condition}")
    st.markdown(f"🌡️  **Temperature**: {temperature} °C ")
    st.markdown(f" 🌬️  **Wind Speed**: {wind_speed} m/s")
    st.markdown(f"💧  **Humidity**: {humidity}% ")

    # You can also display additional weather details if you want to include more data
    # Example: st.markdown(f"**Pressure**: {data['main']['pressure']} hPa")

