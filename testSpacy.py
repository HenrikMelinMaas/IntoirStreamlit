import spacy
from spacy_streamlit import visualize_parser

nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a text")
visualize_parser(doc)