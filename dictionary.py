import streamlit as st
import requests

st.title(" Dictionary App 📚")

# Input word
word = st.text_input("Enter a word:")

# Function to fetch meaning from Free Dictionary API
def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]["meanings"]
        return meanings
    else:
        return None

# Search Button
if st.button("🔍 Search Meaning"):
    if word:
        result = get_meaning(word)
        if result:
            st.success(f"Meanings of '{word}':")
            for meaning in result:
                part_of_speech = meaning["partOfSpeech"]
                st.markdown(f"**{part_of_speech.capitalize()}**")
                for i, definition in enumerate(meaning["definitions"], 1):
                    st.write(f"{i}. {definition['definition']}")
        else:
            st.warning("Meaning not found. Please check the spelling.")
    else:
        st.error("Please enter a word.")
