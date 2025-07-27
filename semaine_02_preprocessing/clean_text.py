import re
import unicodedata
import os

def normalize_unicode(text):
    """
    Normalise les caractères Unicode (accents, symboles, etc.).
    Exemple : "é" devient "e"
    """
    return unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8")


def remove_special_characters(text):
    """
    Supprime les caractères spéciaux, sauf les lettres, chiffres et ponctuations de base.
    """
    return re.sub(r"[^a-zA-Z0-9\s.,!?;:()\"'-]", "", text)


def clean_text(text):
    """
    Nettoie un texte OCR avec plusieurs étapes :
    - Normalisation Unicode
    - Suppression caractères spéciaux
    - Suppression des multiples espaces
    - Passage en minuscules
    """
    text = normalize_unicode(text)
    text = remove_special_characters(text)
    text = re.sub(r"\s+", " ", text)  # supprimer les multiples espaces
    return text.lower().strip()

if __name__ == "__main__":
    # Test rapide
    # sample_text = "L’élève a 95% d’attention ! Déjà vu ? Café ☕️, résumé – très bien."
    # print("Texte original :")
    # print(sample_text)
    # print("\nTexte nettoyé :")
    # print(clean_text(sample_text))
    
    input_path_from_image = "extracted_text.txt"
    input_path_from_pdf = "extracted_text_from_pdf.txt"
    output_path_from_image = os.path.join(os.path.dirname(__file__), "cleaned_text_from_image.txt")
    output_path_from_pdf = os.path.join(os.path.dirname(__file__), "cleaned_text_from_pdf.txt")
    
    try:
        with open(input_path_from_image, "r", encoding="utf-8") as infile:
            raw_text = infile.read()
        cleaned_image = clean_text(raw_text)
        print(f"cleaned_image: {cleaned_image}")
        
        with open(output_path_from_image, "w", encoding="utf-8") as outfile:
            outfile.write(cleaned_image)    
    
    
    except FileNotFoundError:
        print(f"Le fichier {input_path_from_image} est introuvable.")    
    
    try :
        with open(input_path_from_pdf, "r", encoding="utf-8") as infile_pdf:
            raw_text_pdf = infile_pdf.read()
        cleaned_pdf = clean_text(raw_text_pdf)
        print(f"cleaned_pdf: {cleaned_pdf}")
        with open(output_path_from_pdf, "w", encoding="utf-8") as outfile_pdf:
            outfile.write(cleaned_pdf)
    except FileNotFoundError:
        print(f"Le fichier {input_path_from_pdf} est introuvable.")    
    

    print(f"\nTexte nettoyé enregistré dans : {output_path_from_image}")
    print(f"\nTexte nettoyé enregistré dans : {output_path_from_pdf}")
    
   