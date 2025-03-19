import streamlit as st

st.title("🌎Unit Converter App") 
st.markdown("### Converts Length, Weight,Temperature, And Time Instantly")

st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

category = st.selectbox("Choose a category", ["Length", "Weight","Temperature","Time"])

# Define a function to convert units based on category and unit selection
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        
    elif category == "Temperature":
        if unit == "Fahrenheit (°F) to Celsius (°C)":
            return (value - 32) * 5/9
        elif unit == "Celsius (°C) to Fahrenheit (°F)":
            return (value * 9/5) + 32

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
     

# Select the appropriate unit based on the category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", [ "Miles to Kilometers","Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Temperature":
    unit =st.selectbox("🌡 Select Conversion ", ["Fahrenheit (°F) to Celsius (°C)", " Celsius (°C) to Fahrenheit (°F)"])
elif category == "Time":
    unit = st.selectbox("⏲ Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to Days", "Days to Hours"])

value = st.number_input("Enter the value to convert", min_value=0)

# Perform conversion when the button is clicked
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The Result is {result:.2f}")