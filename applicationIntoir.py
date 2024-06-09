# applicationIntoir.py
#
#

import streamlit as st
import spacy
from intoir_Functions import   *

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Set page configuration
st.set_page_config(
    page_title="applicationIntoir",
    layout="wide"
)

# Add title
st.title("Intoir your work situation")

# Add text input field
input_text = st.text_area("Describe your last work situations last six months ?:")

# The
recommendations, mistral_out, mistral_score, construct_score = main_fx (input_text) 


# Display output text
st.markdown(
    f"""
    ## Our recommendation
    
    {recommendations}

    ### Based on 
    """
# Save data 
)
