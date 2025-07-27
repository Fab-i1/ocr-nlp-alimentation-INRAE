# Formation OCR & NLP

### SEMAINE 1

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

### SEMAINE 2

#### 27/07/2025 – Prétraitement du texte OCRisé

Dédiée à la normalisation et au nettoyage des textes extraits via OCR.

### Objectifs :

- Supprimer les caractères spéciaux, accents, sauts de lignes, etc.
- Corriger la casse (minuscules / majuscules)
- Tokenisation de base pour les étapes NLP futures

### Fichiers :

- `semaine_02_preprocessing/clean_text.py` : script principal de nettoyage textuel
  -utilisation des 2 fichiers générés semaine_01 :
  - extract_text.txt (généré depuis une image)
  - extract_text_from_pdf (transformation pdf-->image puis traitement)

### Lancement :

```bash
python semaine_02_preprocessing/clean_text.py
```
