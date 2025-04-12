import streamlit as st
from google import genai
st.header("Unit Convertor")
value1 = st.text_input("Enter Value",placeholder="eg.. length")
value2 = st.text_input("Enter Value",placeholder="eg.. 5 meter")
value3 = st.text_input("Enter Value",placeholder="eg.. centimeter")

# connecting with LLM
Api_Key = st.secrets["API_KEY"]
client = genai.Client(api_key=Api_Key)

if value1 and value2 and value3:



    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=f"you are unit convertor so converts values on {value1},{value2},{value3}.note: your answer must be in digits, don't give explanation"
)
    st.write(f"Output: {response.text}")


