from pdf2image import convert_from_path
from  pytesseract import pytesseract as pyt

import os

# Modifier le chemin vers ton exécutable Tesseract si nécessaire
pyt.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Dossier contenant le fichier PDF
pdf_path = os.path.join(os.path.dirname(__file__),"modele_de_facture.pdf")
print ("Chemin du PDF:", pdf_path)

# Convertir chaque page du PDF en image
images = convert_from_path(pdf_path)
print (f"Nombre de pages converties: {len(images)}")


# # Parcourir les pages et extraire le texte
# for i, image in enumerate(images):
#     text = pyt.image_to_string(image, lang="fra")
#     print(f"\n--- Texte extrait de la page {i+1} ---\n{text}")
