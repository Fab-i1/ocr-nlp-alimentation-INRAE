import os
from clean_text import clean_text
import nltk
from nltk.corpus import stopwords

# Téléchargement des stopwords
nltk.download('stopwords')

def tokenize_text(text):
    """
    Tokenizes the input text into words.
    """
    return text.split()

def remove_stopwords(tokens):
    """
    Removes stopwords from the list of tokens.
    """
    stop_words_en = set(stopwords.words('english'))
    stop_words_fr = set(stopwords.words('french'))
    # print (f"Stop words en: {stop_words_en}")
    # print (f"Stop words fr: {stop_words_fr}")
    return [word for word in tokens if word.lower() not in stop_words_en and word.lower() not in stop_words_fr]

def preprocess_text(text):
    """
    Preprocesses the input text by cleaning, tokenizing, and removing stopwords.
    """
    # Nettoyage du texte
    cleaned_text = clean_text(text)
    
    # Tokenisation
    tokens = tokenize_text(cleaned_text)
    
    # Suppression des stopwords
    tokens_without_stopwords = remove_stopwords(tokens)
    
    return tokens_without_stopwords


if __name__ == "__main__":
    # Fichiers d’entrée/sortie
    input_path_from_image = "extracted_text.txt"
    input_path_from_pdf = "extracted_text_from_pdf.txt"
    output_path_from_image = os.path.join(os.path.dirname(__file__), "preprocessed_text_from_image.txt")
    output_path_from_pdf = os.path.join(os.path.dirname(__file__), "preprocessed_text_from_pdf.txt")

    # Traitement fichier OCR depuis image
    try:
        with open(input_path_from_image, "r", encoding="utf-8") as infile:
            raw_text = infile.read()
        tokens_image = preprocess_text(raw_text)
        with open(output_path_from_image, "w", encoding="utf-8") as outfile:
            outfile.write(" ".join(tokens_image))
        print(f"Texte prétraité (image) enregistré dans {output_path_from_image}")
    except FileNotFoundError:
        print(f"Le fichier {input_path_from_image} est introuvable.")

    # Traitement fichier OCR depuis PDF
    try:
        with open(input_path_from_pdf, "r", encoding="utf-8") as infile_pdf:
            raw_text_pdf = infile_pdf.read()
        tokens_pdf = preprocess_text(raw_text_pdf)
        with open(output_path_from_pdf, "w", encoding="utf-8") as outfile_pdf:
            outfile_pdf.write(" ".join(tokens_pdf))
        print(f"Texte prétraité (PDF) enregistré dans {output_path_from_pdf}")
    except FileNotFoundError:
        print(f"Le fichier {input_path_from_pdf} est introuvable.")
