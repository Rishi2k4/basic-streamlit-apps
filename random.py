import streamlit as st
import random
import string

# App title
st.title(" Random Password Generator 🔐")

# Sidebar for user inputs
st.sidebar.header("Customize Your Password")

# User input options
length = st.sidebar.slider("Password Length", 6, 50, 12)
use_uppercase = st.sidebar.checkbox("Include Uppercase Letters", True)
use_lowercase = st.sidebar.checkbox("Include Lowercase Letters", True)
use_digits = st.sidebar.checkbox("Include Numbers", True)
use_symbols = st.sidebar.checkbox("Include Symbols (!@#$%^&*)", True)

# Character set based on user choices
characters = ''
if use_uppercase:
    characters += string.ascii_uppercase
if use_lowercase:
    characters += string.ascii_lowercase
if use_digits:
    characters += string.digits
if use_symbols:
    characters += "!@#$%^&*()_+-=[]{}|;:,.<>?/"

# Function to generate password
def generate_password(length):
    return ''.join(random.choice(characters) for _ in range(length))

# Generate password on button click
if st.button("Generate Password"):
    if not characters:
        st.error("Please select at least one character type.")
    else:
        password = generate_password(length)
        st.success("Your Random Password:")
        st.code(password, language='text')
