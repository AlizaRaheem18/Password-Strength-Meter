#Project3 Password Strength Meter

import re
import streamlit as st

#styling
st.set_page_config(page_title="Password Strength Meter by Aliza", page_icon="🌘", layout="centered")

st.markdown("""
<style>
     .main{text-align: center;}
     .stTextInput {width: 60% !important; margin: auto;}
     .stButton button {width:50%; background-color #4CAF50; color: white; font-size:18px;}
     .stButton button:hover { background-color: #45a049;}
</style>
""", unsafe_allow_html=True)

#title &description
st.title("🔐 Password Strength Meter")
st.write("Enter your password here to check its security level.✅ ")

#check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be atleast 8 character.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include upper(A-Z) and lower case(a-z).")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include at least one number(0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character(!@#$%^&*).")

    #password strenth result
    if score == 4:
        st.success("✅ Strong Password! Your password is secure.")
    elif score == 3:
        st.info("⚠️ Moderate Password! Consider improving security by adding more feature.")
    else:
        st.error("❌ Week Password! Follow the suggestion below to strength it.")

    #feedback
    if feedback:
        with st.expander("🔍 Improve Your Password "):
            for item in feedback:
                st.write(item)
    password = st.text_input("Enter Your Password:", type="password", help="Ensure your password is strong 🔒")

#button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning(" ⚠️ Please enter a password first!")
