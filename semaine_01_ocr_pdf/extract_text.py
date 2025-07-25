import os
from PIL import Image
import pytesseract

# Chemin Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Chemin vers le dossier local tessdata
tessdata_path = os.path.join(os.path.dirname(__file__), "tessdata")
print("TESSDATA path:", tessdata_path)
print("Contenu du dossier tessdata:", os.listdir(tessdata_path))

os.environ["TESSDATA_PREFIX"] = tessdata_path


image_path = r"C:\Users\fab\Pictures\INRAE\ticket_de_caisse.jpg"

# Image test
image = Image.open(image_path)

# OCR
text = pytesseract.image_to_string(image, lang="fra")
print(text)
