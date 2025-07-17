import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

# Title
st.title("🗺️ Interactive Map with Folium")

# Input location
location_input = st.text_input("Enter a location:", "Stockholm, Sweden")

# Create geolocator
geolocator = Nominatim(user_agent="map_app")

# Get coordinates
location = geolocator.geocode(location_input)

if location:
    lat, lon = location.latitude, location.longitude

    # Create map
    m = folium.Map(location=[lat, lon], zoom_start=13)
    folium.Marker([lat, lon], tooltip=location.address, popup="📍 You are here!").add_to(m)

    # Display map
    st_folium(m, width=700, height=500)
else:
    st.error("Location not found. Try something else.")
