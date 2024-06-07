# testSpacy within streamlit
import streamlit as st
import spacy 

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

st.title('SpaCy with Streamlit')

# Text input
user_input = st.text_area("Enter text:", "Type something here...")

# Process text with SpaCy
if user_input:
    doc = nlp(user_input)
    
    # Display the named entities
    st.header("Named Entities")
    for ent in doc.ents:
        st.write(f'{ent.text} ({ent.label_})')
