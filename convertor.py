#Project 1:Unit Convertor
#Build a google unit convertor using python and streamlit:

import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
   }
   .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding:30px;
        border-radius:15px;
        box-shadow:0px 10px 30px rgba(0,0,0,0.3);
   }
   h1 {
        text-align:centre;
        font-size:36px;
        color:white;
   }
   .stBtton>button{
        background:linear-gradient(45deg, #0b5394, #351c75);
        color:black;
        font-size:18px;
        padding:10px 20px;
        border-radius:10px;
        transition:0.3s;
        box-shadow:0px 5px 15px rgba(0,201,255,0.4);
   }
   .stButton>button:hover {
        transform:scale(1.05);
        background:linear-gradient(45deg,rgb(15, 109, 196),rgb(229, 241, 245));
        color:black;
   }
   .result-box{
        font-size:20px;
        font-weight:bold;
        text-align:centre;
        background: grey;
        padding:25px;
        border-radius:10px;
        margin-top:20px;
        box-shadow: 0px 5px 15px rgba(0,201,255,0.3)
   }
   .footer{
        text-align:centre;
        margin-top:50px;
        font-size:14px;
        color:black;
   }
   </style>
   """,
   unsafe_allow_html=True
)
#title & description
st.markdown("<h1> Unit Convertor</h1>", unsafe_allow_html = True)
st.write("Convert between different units of length , weight, and temprature.")

#sidebar menu
conversation_type = st.sidebar.selectbox("Choose Conversation Type", ["Length", "Weight", "Temprature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversation_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilograms","Centimeters","Milimeters","Miles","Yards","Inches","Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilograms","Centimeters","Milimeters","Miles","Yards","Inches","Feet"])
elif conversation_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams","Miligrams" "pounds","Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams","Miligrams" "pounds","Ounces"])
elif conversation_type == "Temprature":
    with col1:
        from_unit = st.selectbox("From", ["Celsis", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsis", "Fahrenheit", "Kelvin"])

#converted function
def length_convertor(value, from_unit, to_unit):
    length_units = {
        'Meters' : 1, 'Kilometers':0.001, 'Centemeters':100, 'Milimeters':1000,
        'Miles':0.000621371, 'Yards':1.09636, 'Feet':3.28, 'Inches':39.37
    }
    return ( value / length_units[from_unit] ) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        'Kilogram':1, 'Gram':1000, 'Miligram':1000000, 'pounds':2.2046, 'Ounces':35.27
    }
    return(value / weight_units[from_unit]) * weight_units[to_unit]

def temp_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return(value * 9/5 +32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return(value-32) * 5/9 if to_unit == "Celcius" else (value-32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celcius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

if st.button("🔁 Convert"):
    result = None  # Initialize result variable to avoid NameError
    if conversation_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversation_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversation_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)

    if result is not None:
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
    else:
        st.error("Conversion error. Please check input values.")

st.markdown("<div class='footer'>Created by Aliza.</div>", unsafe_allow_html=True)

