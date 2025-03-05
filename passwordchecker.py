import re
import streamlit as st

# Styling
st.set_page_config(page_title="Password Strength Meter by Aliza", page_icon="🌘", layout="centered")

st.markdown("""
 <style>
      .main{text-align: center;}
      .stTextInput {width: 60% !important; margin: auto;}
     .stButton button {width:50%; background-color: blue; color: white; font-size:18px;}
     .stButton button:hover { background-color: yellow; color:white;}
 </style>

""", unsafe_allow_html=True)

# Title & description
st.title("🔐 Password Strength Meter")
st.write("Enter your password here to check its security level.✅ ")

# Password input (moved outside the function)
password = st.text_input("Enter Your Password:", type="password", help="Ensure your password is strong 🔒")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include both uppercase (A-Z) and lowercase (a-z) letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Password strength result
    if score == 4:
        st.success("✅ Strong Password! Your password is secure.")
    elif score == 3:
        st.info("⚠️ Moderate Password! Consider improving security by adding more features.")
    else:
        st.error("❌ Weak Password! Follow the suggestions below to strengthen it.")

    # Feedback
    if feedback:
        with st.expander("🔍 Improve Your Password "):
            for item in feedback:
                st.write(item)

# Button functionality
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")

