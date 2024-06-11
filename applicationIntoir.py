# applicationIntoir.py 
# v004
#

import streamlit as st
import spacy
import streamlit.components.v1 as components
from intoir_Functions import   *
input_text = "And Crispin Crispian shall neer go by, From this day to the ending of the world, But we in it shall be remember We few, we happy few, we band of brothers"
# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Set page configuration
st.set_page_config(
    page_title="applicationIntoir",
    layout="wide"
)

# Add title

st.title("Describe your work situations  for the last six months ? ")

# Add text input field
input_text = st.text_area(" Intoir your work situation v004:")

# Check if the input text length is greater than 100 characters
if len(input_text) > 100:
    st.success("Lets proceed!")
else:
    st.warning("Please enter at least 60 words")

# Add a button to simulate an action that should only proceed if the condition is met
if st.button("OK"):
    if len(input_text) > 100:
        st.write("Proceeding with the action...")
        # Add your logic here for what happens when the user clicks OK
    else:
        st.error("The text must be long.")

# The
recommendations, mistral_out, mistral_score, construct_score = main_fx (input_text) 

# View 
outhtml = make_html_recommendations (construct_score)
components.html(outhtml, height=430) 
