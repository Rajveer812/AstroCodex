# app.py
import streamlit as st
import datetime
from services.weather_api import get_forecast
from utils.helpers import process_forecast
from ui.components import show_result

st.title("🌦️ Will It Rain On My Parade?")

city = st.text_input("Enter City:")
date = st.date_input("Select Date:", datetime.date.today())

if st.button("Check Weather"):
    if not city:
        st.error("⚠️ Please enter a city name")
    else:
        data = get_forecast(city)
        if not data:
            st.error("❌ Failed to fetch data. Check city name or API key.")
        else:
            target_date = date.strftime("%Y-%m-%d")
            weather = process_forecast(data, target_date)
            if not weather:
                st.warning("⚠️ No forecast data for this date (try within 5 days).")
            else:
                show_result(city, target_date, weather)
