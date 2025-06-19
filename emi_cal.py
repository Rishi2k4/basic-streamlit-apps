import streamlit as st
import math
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Loan EMI Calculator", page_icon="🏦", layout="centered")

# Title
st.title("🏦 Loan EMI Calculator")
st.markdown("Easily calculate your monthly loan payments and total interest.")

# Sidebar Inputs
st.sidebar.header("Loan Parameters")
loan_amount = st.sidebar.number_input("Loan Amount (₹)", min_value=1000.0, value=500000.0, step=1000.0, format="%.2f")
annual_interest = st.sidebar.slider("Annual Interest Rate (%)", min_value=0.0, max_value=20.0, value=7.5, step=0.1)
loan_tenure_years = st.sidebar.slider("Loan Tenure (Years)", min_value=1, max_value=30, value=10)

# EMI Calculation
monthly_interest = annual_interest / (12 * 100)
loan_tenure_months = loan_tenure_years * 12

if monthly_interest == 0:
    emi = loan_amount / loan_tenure_months
else:
    emi = loan_amount * monthly_interest * ((1 + monthly_interest) ** loan_tenure_months) / (((1 + monthly_interest) ** loan_tenure_months) - 1)

total_payment = emi * loan_tenure_months
total_interest = total_payment - loan_amount

# Results
st.subheader("📊 Loan Summary")

col1, col2 = st.columns(2)
col1.metric("Monthly EMI", f"₹{emi:,.2f}")
col2.metric("Loan Tenure", f"{loan_tenure_months} months")

col3, col4 = st.columns(2)
col3.metric("Total Interest", f"₹{total_interest:,.2f}")
col4.metric("Total Payment", f"₹{total_payment:,.2f}")

# Pie Chart
st.subheader("📈 Principal vs Interest")

fig = px.pie(
    names=["Principal Amount", "Total Interest"],
    values=[loan_amount, total_interest],
    color_discrete_sequence=px.colors.sequential.RdBu,
    hole=0.4
)
st.plotly_chart(fig, use_container_width=True)

st.caption("Built with ❤️ using Streamlit")
