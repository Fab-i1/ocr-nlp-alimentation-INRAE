# Formation OCR & NLP
Programme de formation sur plusieurs semaines
Semaine 1 – Bases OCR et extraction
Comprendre ce qu’est l’OCR et comment fonctionne l’extraction de texte depuis des images ou PDF.
Pratique : extraire du texte brut à partir de fichiers PDF ou images avec Python.

Semaine 2 – Nettoyage et prétraitement de texte
Nettoyage des textes bruts : normalisation Unicode, suppression des caractères spéciaux, suppression des espaces et ponctuations superflues, mise en minuscules.
Exercices pratiques avec la fonction clean_text().
Introduction à spaCy pour tokenisation et lemmatisation.

Semaine 3 – Prétraitement avancé avec spaCy
Tokenisation avancée, suppression de stopwords, lemmatisation.
Gestion multilingue (FR/EN).
Exercices : produire des listes de tokens exploitables pour NLP.

Semaine 4 – Extraction d’informations
Identifier les champs importants dans les documents (SIRET, TVA, montants, dates).
Utilisation de regex et règles pour extraction automatique.
Exercices : construire un dictionnaire clé → valeur pour chaque document.

Semaine 5 – Structuration et stockage
Stocker les données extraites sous forme de JSON ou CSV.
Vérification de la qualité des données extraites.
Exercices : sauvegarde et relecture des données structurées.

Semaine 6 – Analyse NLP ou apprentissage automatique (optionnel)
Transformer les textes en vecteurs (TF-IDF, embeddings).

Premiers modèles simples de classification ou clustering.
Exercices : analyse exploratoire et visualisation des données textuelles.

## SEMAINE 1

### 25/07/2025 – OCR sur image (PNG)

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

### Objectifs

- Supprimer les caractères spéciaux, accents, sauts de lignes, etc.
- Corriger la casse (minuscules / majuscules)
- Tokenisation de base pour les étapes NLP futures

### Fichiers

- `semaine_02_preprocessing/clean_text.py` : script principal de nettoyage textuel
  -utilisation des 2 fichiers générés semaine_01 :
  - extract_text.txt (généré depuis une image)
  - extract_text_from_pdf (transformation pdf-->image puis traitement)

- 18/08/2025, tokénisation de base pour les futures étapes NLP avec le fichier preprocessing.py
  - utilisation des fichiers de sortie générés par clean_text.py :
    - `cleaned_text_from_image.txt` --> `preprocessed_with_spacy_cleaned_text_from_image.txt`
    - `cleaned_text_from_pdf.txt` --> `preprocessed_with_spacy_cleaned_text_from_image.txt`

- 23/08/2025:
  - README : mise à jour pour refléter l'état actuel du projet
  - Scripts Python :
    - mise à jour de clean_text.py :
      - normalisation des dates
      - Normalisation Unicode
      - Suppression des caractères spéciaux
      - Nettoyage des espaces et mise en minuscules
    - mise à jour de préprocessing.py avec utilisation de SpaCy
      - Préparation pour l'extraction d'informations structurées (SIRET, TVA, montants, dates, adresses, téléphone)

--> Pour générer les fichiers :

  ```bash
  python semaine_02_preprocessing/clean_text.py
  ```

--> pour tokénisation :

  ```bash
  python semaine_02_preprocessing/preprocessing.py
  ```
