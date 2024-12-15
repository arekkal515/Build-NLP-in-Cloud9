import wikipedia
import nltk
from textblob import TextBlob

text_blob = wikipedia.summary("Golden State Warriors")
blob = TextBlob(text_blob)
blob_noun_phrases = blob.noun_phrases

print(blob_noun_phrases)

#blob.tags