import streamlit as st
from google import genai
st.header("Password Strength Meter")
value1 = st.text_input("Enter Password",placeholder="kLmnpkrsy7_$7sd")

# connecting with LLM
Api_Key = st.secrets["API_KEY"]
client = genai.Client(api_key=Api_Key)

if value1:

    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=f"""

        You are Password Strength Meter that evaluates a user's password based on security rules.
        user password is: {value1}
        🔹 Requirements
1. Password Strength Criteria
A strong password should:
✅ Be at least 8 characters long
✅ Contain uppercase & lowercase letters
✅ Include at least one digit (0-9)
✅ Have one special character (!@#$%^&*)

2. Scoring System
Weak (Score: 1-2) → Short, missing key elements
Moderate (Score: 3-4) → Good but missing some security features
Strong (Score: 5) → Meets all criteria
3. Feedback System
If the password is weak, suggest improvements.
If the password is strong, display a success message.

don't give explanation. 
    """
)
    st.write(f"Output: {response.text}")
