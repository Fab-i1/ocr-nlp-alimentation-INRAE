# ######################################################################
# Ce script effectue le prétraitement de texte OCR en français et en anglais à l'aide de nltk une première fois 
#  avec modification du script le 23/08/2025 pour utilisation de spaCy.
# Fonctionnalités principales :
# - Nettoyage, tokenisation, lemmatisation, mise en minuscules
# - Prise en charge des fichiers texte extraits d'images et de PDF
# - Enregistrement du texte prétraité dans des fichiers de sortie
# Fonctions :
# - preprocess_text_with_spacy(text, lang='en'): 
#     Prend un texte brut et une langue ('fr' ou 'en'), retourne une liste de tokens lemmatisés, nettoyés et filtrés.
# Utilisation :
# - Définir les fichiers d'entrée et leur langue associée
# - Pour chaque fichier existant, appliquer le prétraitement et sauvegarder le résultat
# Dépendances :
# - spaCy et les modèles 'fr_core_news_sm' et 'en_core_web_sm'
# - os
# Auteur : Modification du script le 23/08/2025 pour utilisation de spaCy
# ######################################################################

# import os
# from clean_text import clean_text
# #import nltk
# #from nltk.corpus import stopwords
# import spacy

# # Téléchargement des stopwords
# #nltk.download('stopwords')

# # def tokenize_text(text):
# #     """
# #     Tokenizes the input text into words.
# #     """
# #     return text.split()

# # def remove_stopwords(tokens):
# #     """
# #     Removes stopwords from the list of tokens.
# #     """
# #     stop_words_en = set(stopwords.words('english'))
# #     stop_words_fr = set(stopwords.words('french'))
# #     # print (f"Stop words en: {stop_words_en}")
# #     # print (f"Stop words fr: {stop_words_fr}")
# #     return [word for word in tokens if word.lower() not in stop_words_en and word.lower() not in stop_words_fr]

# def preprocess_text(text):
#     """
#     Preprocesses the input text by cleaning, tokenizing, and removing stopwords.
#     """
#     # Nettoyage du texte
#     cleaned_text = clean_text(text)
    
#     # Tokenisation
#     tokens = tokenize_text(cleaned_text)
    
#     # Suppression des stopwords
#     tokens_without_stopwords = remove_stopwords(tokens)
    
#     return tokens_without_stopwords


# if __name__ == "__main__":
#     # Fichiers d’entrée/sortie
#     input_path_from_image = "semaine_02_preprocessing\cleaned_text.txt"
#     input_path_from_pdf = "semaine_02_preprocessing\cleaned_text_from_pdf.txt"
#     output_path_from_image = os.path.join(os.path.dirname(__file__), "preprocessed_text_from_image.txt")
#     output_path_from_pdf = os.path.join(os.path.dirname(__file__), "preprocessed_text_from_pdf.txt")

#     # Traitement fichier OCR depuis image
#     try:
#         with open(input_path_from_image, "r", encoding="utf-8") as infile:
#             raw_text = infile.read()
#         tokens_image = preprocess_text(raw_text)
#         print(f"Tokens après prétraitement (image): {tokens_image[:10]}...")  # Affiche les 10 premiers tokens pour vérification
#         with open(output_path_from_image, "w", encoding="utf-8") as outfile:
#             outfile.write(" ".join(tokens_image))
#         print(f"Texte prétraité (image) enregistré dans {output_path_from_image}")
#     except FileNotFoundError:
#         print(f"Le fichier {input_path_from_image} est introuvable.")

#     # Traitement fichier OCR depuis PDF
#     try:
#         with open(input_path_from_pdf, "r", encoding="utf-8") as infile_pdf:
#             raw_text_pdf = infile_pdf.read()
#         tokens_pdf = preprocess_text(raw_text_pdf)
#         with open(output_path_from_pdf, "w", encoding="utf-8") as outfile_pdf:
#             outfile_pdf.write(" ".join(tokens_pdf))
#         print(f"Texte prétraité (PDF) enregistré dans {output_path_from_pdf}")
#     except FileNotFoundError:
#         print(f"Le fichier {input_path_from_pdf} est introuvable.")

import os
import spacy

# Charger les modèles FR et EN
nlp_models = {
    "fr": spacy.load("fr_core_news_sm"),
    "en": spacy.load("en_core_web_sm")
}

def preprocess_text_with_spacy(text, lang='en'):
    """
    Prétraitement du texte avec spaCy :
    - Tokenisation
    - Lemmatisation
    - Mise en minuscules
    - Suppression des stopwords, ponctuation et espaces
    """
    nlp = nlp_models[lang]
    doc = nlp(text)
    
    tokens = [
        token.lemma_.lower()        # on garde la lemmatisation et on met en minuscules
        for token in doc            # on filtre les stopwords, ponctuation et espaces
        if not token.is_stop        
        and not token.is_punct      # on enlève la ponctuation
        and not token.is_space      # on enlève les espaces
    ]
    return tokens


if __name__ == "__main__":
    files = [
        ("semaine_02_preprocessing\cleaned_text_from_image.txt", "fr"),        # fichier français
        ("semaine_02_preprocessing\cleaned_text_from_pdf.txt", "en") # fichier anglais
    ]

    for input_file, lang in files:
        if os.path.exists(input_file):
            with open(input_file, "r", encoding="utf-8") as f:
                raw_text = f.read()
            
            tokens = preprocess_text_with_spacy(raw_text, lang=lang)
            output_file = f"preprocessed_with_spacy_{os.path.basename(input_file)}"
            with open(output_file, "w", encoding="utf-8") as out_f:
                out_f.write(" ".join(tokens))
            
            print(f"Texte prétraité ({lang}) enregistré dans {output_file}")
        else:
            print(f"Le fichier {input_file} est introuvable.")
