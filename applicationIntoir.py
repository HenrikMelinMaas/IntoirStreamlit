# applicationIntoir.py 002
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
st.title("Intoir your work situation v002")

# Add text input field
input_text = st.text_area("Describe your last work situations last six months ?:")

# Check if the input text length is greater than 100 characters
if len(input_text) > 100:
    st.success("Text is more than 100 characters. You can proceed!")
else:
    st.warning("Please enter at least 100 characters.")

# Add a button to simulate an action that should only proceed if the condition is met
if st.button("OK"):
    if len(input_text) > 100:
        st.write("Proceeding with the action...")
        # Add your logic here for what happens when the user clicks OK
    else:
        st.error("The text must be more than 100 characters before proceeding.")

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
