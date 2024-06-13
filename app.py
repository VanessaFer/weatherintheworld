import streamlit as st
import json
import requests

st.set_page_config(
    page_title="Predici il meteo",
    page_icon=":sun_small_cloud:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

###### CSS BACKGROUND #######################
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://nananwallpaper.it/wp-content/uploads/2018/10/5-Pattern-a-cuori-azzurro-chiaro-Carta-da-parati-Baby-Interior-Design-Wallpaper%C2%AE-per-Nana%CC%81n%C2%AE-1-Dettaglio-01-01.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

st.title("Predici il meteo!")

API_key = "04ee6d6ae668b722c39a1cde0d86fb9e"

city_name = st.text_input("Scrivi il nome della città:")
#st.write(city_name)

def weather_var(city_val):
    lon = json["coord"].get("lon")
    lat = json["coord"].get("lat")
    temp = json["main"].get("temp")
    temp = temp - 273.15
    temp = round(temp, 1)
    temp_percepita = json["main"].get("feels_like")
    temp_percepita = temp_percepita - 273.15
    temp_percepita = round(temp_percepita, 1)
    temp_minima = json["main"].get("temp_min")
    temp_minima = temp_minima - 273.15
    temp_minima = round(temp_minima, 1)
    temp_massima = json["main"].get("temp_max")
    temp_massima = temp_massima - 273.15
    temp_massima = round(temp_massima, 1)
    pressione = json["main"].get("pressure")
    umidita = json["main"].get("humidity")
    visibilita = json["visibility"]
    wind_speed = json["wind"].get("speed")
    wind_deg = json["wind"].get("deg")
    clouds_all = json["clouds"].get("all")
    return city_val

if city_name:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
    result = requests.get(url)
    json = result.json()
    #st.write(weather_var())
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Temperatura effettiva")
        st.write("La temperatura effettiva al", city_name, "è", round(((json["main"].get("temp"))-273.15),1), "°.")

    with col2:
            st.subheader("Temperatura percepita")
            st.write("La temperatura percepita al", city_name, "è", round(((json["main"].get("feels_like"))-273.15),1), "°.")

    with col1:
        st.subheader("Temperatura Minima")
        st.write("La temperatura minima di", city_name, "è", round(((json["main"].get("temp_min"))-273.15),1), "°.")
    
    with col2:
        st.subheader("Temperatura Massima")
        st.write("La temperatura massima di", city_name, "è", round(((json["main"].get("temp_max"))-273.15),1), "°.")
    
    tab1, tab2, tab3 = st.tabs(["Pressione", "Umidità", "Visibilità"])

    with tab1:
        st.subheader("Pressione")
        st.write("La pressione a", city_name, "è di", json["main"].get("pressure"), "hPa.")

    with tab2:
        st.subheader("Umidità")
        st.write("La umidità a", city_name, "è del", json["main"].get("humidity"), "%.")

    with tab3:
        st.subheader("Visibilità")
        st.write("La visibilità a", city_name, "è di", json["visibility"], "m.")

        
        



