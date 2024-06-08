#import spacy
#from spacy_streamlit import visualize_parser
import streamlit as st
import spacy

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

st.title('SpaCy with Streamlit  en_core_web_sm')
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a text")
#visualize_parser(doc)