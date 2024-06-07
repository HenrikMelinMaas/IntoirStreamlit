# testSpacy within streamlit
import streamlit as st
import spacy_streamlit as spacy

models = ["en_core_web_sm", "en_core_web_md"]
default_text = "Sundar Pichai is the CEO of Google."
spacy.visualize(models, default_text)
