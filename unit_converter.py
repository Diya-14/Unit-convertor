import streamlit as st
from deep_translator import GoogleTranslator

# Unit Conversion Data
unit_conversions = {
    "Length": {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701
    },
    "Weight": {
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1e6,
        "pounds": 2.20462,
        "ounces": 35.274
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    }
}

def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius":
            return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
        elif from_unit == "Fahrenheit":
            return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    else:
        return value * (unit_conversions[category][to_unit] / unit_conversions[category][from_unit])

# Streamlit UI
st.title("🌎 Google-Like Unit Converter")

# Sidebar
st.sidebar.header("Select Conversion Type")
category = st.sidebar.selectbox("Choose Category", list(unit_conversions.keys()))

# User Inputs
st.subheader(f"Convert {category}")
from_unit = st.selectbox("From", list(unit_conversions[category].keys()))
to_unit = st.selectbox("To", list(unit_conversions[category].keys()))
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Conversion & Display
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"💡 {value} {from_unit} = {result:.2f} {to_unit}")

# Translator Feature
st.sidebar.header("🌍 Translate Result")
translate_text = st.sidebar.text_input("Enter text to translate:")
target_language = st.sidebar.text_input("Enter target language code (e.g., 'es' for Spanish, 'fr' for French)")

if st.sidebar.button("Translate"):
    if translate_text and target_language:
        translated = GoogleTranslator(source="auto", target=target_language).translate(translate_text)
        st.sidebar.success(f"Translation: {translated}")
    else:
        st.sidebar.warning("Please enter text and a language code.")
