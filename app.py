import streamlit as st
import re
# Function to check password strength
def check_password_strength(password: str) -> dict:
    strength = 0
    criteria = [
        (r"[a-z]", "Lowercase Letter"),
        (r"[A-Z]", "Uppercase Letter"),
        (r"\d", "Digit"),
        (r"[@$!%*?&]", "Special Character"),
        (r".{8,}", "Minimum 8 Characters")
    ]
    
    passed_criteria = [desc for pattern, desc in criteria if re.search(pattern, password)]
    strength = len(passed_criteria) * 20
    return {"strength": strength, "criteria": passed_criteria}

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="wide")

# Custom CSS for better UI
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stTextInput > div > div > input {
            background-color: white !important;
            border: 2px solid #2E86C1 !important;
            padding: 10px !important;
            border-radius: 10px !important;
        }
        .stButton > button {
            background-color: white !important;
            color: #2E86C1 !important;
            border: 2px solid #2E86C1 !important;
            border-radius: 10px !important;
            padding: 10px 20px !important;
            font-size: 16px !important;
            font-weight: bold !important;
            cursor: pointer !important;
        }
        .stButton > button:hover {
            background-color: #2E86C1 !important;
            color: white !important;
        }
        .header {
            margin-top: -70px;
        }
        .sidebar .sidebar-content {
            background-color: #e3f2fd;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Adjusted Header Position
st.markdown("""
    <div class='header'>
        <h1 style='text-align: center; color: #2E86C1;'>🔐 Password Strength Meter</h1>
        <h2 style='text-align: center; color: #2E86C1;'>🔑 Secure Your Digital Identity</h2>
        <p style='text-align: center; color: gray;'>A strong password is your first defense against cyber threats. Use our tool to check and improve your password security.</p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.write("Enter a password to check its strength:")
    st.write("\n\n\n")  # Adds more space below the input field
    
    password = st.text_input("Password", type="password")
    check_button = st.button("Check Password Strength")
    st.write("\n\n")  # Adds more space below input field
    
    if check_button and password:
        result = check_password_strength(password)
        strength = result["strength"]
        color = "#2E86C1" if strength <= 40 else "orange" if strength <= 80 else "green"
        
        st.progress(strength / 100)
        st.markdown(f"<h3 style='color: {color};'>Strength: {strength}%</h3>", unsafe_allow_html=True)
        
        st.write("### Criteria met:")
        for criteria in result["criteria"]:
            st.markdown(f"✅ {criteria}")
        
        if strength == 100:
            st.success("Your password is strong!")
        else:
            st.warning("Try adding more complexity!")

with col2:
    st.write("\n\n\n")  # Adds more space between sidebar and content
    st.write("## Tips for a Strong Password:")
    st.markdown("""
    - ✅ Use at least **8 characters**.
    - 🖀 Include **uppercase & lowercase letters**.
    - 🖒 Add **numbers** and **special symbols** (@, $, !, etc.).
    - 🚫 Avoid common words (e.g., "password123").
    - 🔄 Use a **passphrase** instead of a single word.
    - 🛡️ Consider using a **password manager**.
    """)

# Footer with developer name
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 10px;
            width: 100%;
            text-align: center;
            font-size: 16px;
            color: gray;
        }
    </style>
    <div class='footer'>Developed by <b>Yasir</b> 🚀</div>
""", unsafe_allow_html=True)