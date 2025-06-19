import streamlit as st
from textblob import TextBlob

# App title
st.title("💬 Text Sentiment Analyzer")
st.markdown("Analyze the **sentiment** of your text: Positive, Negative, or Neutral.")

# Text input
user_input = st.text_area("Enter your text here:")

# Analyze button
if st.button("🔍 Analyze Sentiment"):
    if user_input.strip() != "":
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        st.subheader("🧠 Sentiment Result")

        if polarity > 0:
            st.success("Sentiment: **Positive** 😊")
        elif polarity < 0:
            st.error("Sentiment: **Negative** 😠")
        else:
            st.info("Sentiment: **Neutral** 😐")

        st.markdown(f"**Polarity Score:** `{polarity:.2f}`")
    else:
        st.warning("Please enter some text to analyze.")
