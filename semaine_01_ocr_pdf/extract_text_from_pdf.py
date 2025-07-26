from pdf2image import convert_from_path
import pytesseract

import os

# # Modifier le chemin vers ton exécutable Tesseract si nécessaire
# pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Chemin Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Chemin vers le dossier local tessdata
tessdata_path = os.path.join(os.path.dirname(__file__), "tessdata")
print("TESSDATA path:", tessdata_path)
print("Contenu du dossier tessdata:", os.listdir(tessdata_path))

os.environ["TESSDATA_PREFIX"] = tessdata_path


# Dossier contenant le fichier PDF
pdf_path = os.path.join(os.path.dirname(__file__),"modele_de_facture.pdf")
print ("Chemin du PDF:", pdf_path)

# Convertir chaque page du PDF en image
images = convert_from_path(pdf_path)
print (f"Nombre de pages converties: {len(images)}")

with open("extracted_text_from_pdf.txt", "w", encoding="utf-8") as f:
    # Parcourir les pages et extraire le texte
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, lang="fra")
        print(f"\n--- Texte extrait de la page {i+1} ---\n{text}")
        f.write(f"\n--- Texte extrait de la page {i+1} ---\n{text}")