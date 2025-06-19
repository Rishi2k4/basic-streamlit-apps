import streamlit as st

# Title
st.title(" BMI Calculator 💪")

# Input: Height (in cm) and Weight (in kg)
height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=300.0, step=0.1)
weight = st.number_input("Enter your weight (in kg):", min_value=10.0, max_value=300.0, step=0.1)

# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        height_m = height / 100  # Convert height to meters
        bmi = weight / (height_m ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        # BMI Category
        if bmi < 18.5:
            st.info("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obese")
    else:
        st.error("Please enter valid height and weight.")
