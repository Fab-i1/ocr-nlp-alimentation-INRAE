# Formation OCR & NLP

### Semaine 1

#### 25/07/2025 – OCR sur image (PNG)

- Script `extract_text.py` permettant d'extraire du texte depuis une image à l'aide de Tesseract OCR.
- **Prérequis :**
  - Python 3.9+
  - Tesseract installé localement
  - Fichier `fra.traineddata` à placer dans `semaine_01_ocr_pdf/tessdata/`
- **Installation des dépendances :**
  ```bash
  pip install pillow pytesseract
  ```

#### 26/07/2025 – OCR depuis un PDF

- Extraction de texte depuis des fichiers PDF (via `extract_text_from_pdf.py` + `pdf2image`)
- Tesseract installé localement
- Fichier `fra.traineddata` à placer dans `semaine_01_ocr_pdf/tessdata/`
