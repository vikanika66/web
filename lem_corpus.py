import nltk
# nltk.download("stopwords")
"""
Creates a corpus of data.
This programs reads all paths in data directory and all files in subdirectories.
After that script normalize and preprocess all documents to create a corpus file.
It will take ~40-60 min to complete this script.
"""
from pymystem3 import Mystem
from nltk.corpus import stopwords
from string import punctuation
from bs4 import BeautifulSoup
import os
import re

stem = Mystem()
stop = set(stopwords.words("russian"))
stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '#', '№', '*', '_', '\n'])

path = "data/ffs"
total_corpus = []
corpus = []
PATHS = []
PREPARED_CORPUS_PATH = 'data/prepared_corpus.txt'
