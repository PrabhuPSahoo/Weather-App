import streamlit as st
from modules.api_handler import get_weather_data
from modules.ui_components import weather_form, display_weather
from modules.utils import convert_temperature

# Add custom CSS to change the background color and make it a dark theme
st.markdown(
    """
    <style>
    /* Set the background color to dark */
    body {
        background-color: #121212;
        color: white;
    }
    
    /* Button style */
    button, .stButton>button {
        background-color: #333;
        color: white;
        border: 1px solid #444;
    }

    /* Input field style */
    input, .stTextInput>div>input {
        background-color: #333;
        color: white;
        border: 1px solid #444;
    }

    /* Text input label color */
    .stTextInput>div>label {
        color: white;
    }

    /* Heading style */
    .stTitle, .stHeader {
        color: white;
    }

    /* Error message style */
    .stError {
        background-color: #ff4d4d;
        color: white;
    }

    /* Icon style for weather condition */
    .weather-icon {
        font-size: 40px;
        margin-right: 10px;
    }

    </style>
    """, unsafe_allow_html=True
)

# Function to display weather icon based on the weather condition
def get_weather_icon(weather_condition):
    icons = {
        "Clear": "☀️",  # Sun icon
        "Clouds": "☁️",  # Cloud icon
        "Rain": "🌧️",  # Rain icon
        "Snow": "❄️",  # Snowflake icon
        "Thunderstorm": "⚡",  # Lightning icon
        "Drizzle": "🌦️",  # Drizzle icon
    }
    return icons.get(weather_condition, "🌍")  # Default to Earth icon if unknown

# Streamlit App Interface
def main():
    st.title("Weather App 🏙️")

    # Collect city input from user
    city = weather_form()

    if city:
        # Get weather data
        data = get_weather_data(city)

        if data:
            temperature_celsius = data["main"]["temp"]

            # Display weather information with icons using the updated display_weather function
            display_weather(data, temperature_celsius)

        else:
            st.error("Invalid city name. Please try again.")

if __name__ == "__main__":
    main()
