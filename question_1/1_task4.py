# Github repository: https://github.com/19rafsan97/HIT137_Assignment_2

import spacy
from transformers import pipeline

# Load SpaCy models
nlp_sci = spacy.load("en_core_sci_sm")
nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")
biobert_model = pipeline("ner", model="dmis-lab/biobert-v1.1")

# Function to extract diseases and drugs
def extract_entities(text, model):
    # Initialize lists for entities
    diseases = []
    drugs = []
    
    # Split the text into chunks and process each chunk
    chunk_size = 1000000  # Adjust this size based on your needs
    for start in range(0, len(text), chunk_size):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        doc = model(chunk)
        diseases.extend([ent.text for ent in doc.ents if ent.label_ == 'DISEASE'])
        drugs.extend([ent.text for ent in doc.ents if ent.label_ == 'CHEMICAL'])
    
    return diseases, drugs

# Read the text file
with open('output_text.txt', 'r') as file:
    text = file.read()

# Extract entities using the two models
diseases_sci, drugs_sci = extract_entities(text, nlp_sci)
diseases_bc5cdr, drugs_bc5cdr = extract_entities(text, nlp_bc5cdr)

# Extract NER entities with BioBERT
entities_biobert = biobert_model(text)
diseases_biobert = [ent['word'] for ent in entities_biobert if 'DISEASE' in ent['entity']]
drugs_biobert = [ent['word'] for ent in entities_biobert if 'DRUG' in ent['entity']]

# Compare results
print("SciSpaCy - Diseases:", diseases_sci)
print("SciSpaCy - Drugs:", drugs_sci)
print("BC5CDR - Diseases:", diseases_bc5cdr)
print("BC5CDR - Drugs:", drugs_bc5cdr)
print("BioBERT - Diseases:", diseases_biobert)
print("BioBERT - Drugs:", drugs_biobert)
