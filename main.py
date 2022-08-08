
from bs4 import BeautifulSoup #HTML parsing
import spacy #Just a great library for NLP
import unidecode # accepts unicode string values and returns a unicode string
from word2number import w2n #As the name says
import contractions #Don't -> Do not

# load spacy model, can be "en_core_web_sm" as well
nlp = spacy.load('en_core_web_md')