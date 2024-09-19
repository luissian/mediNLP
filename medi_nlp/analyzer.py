# medi_nlp/analyzer.py
import spacy

class Analyzer:
    def __init__(self):
        # Load spaCy model for English
        self.nlp = spacy.load('en_core_web_sm')

    def analyze_text(self, text:str) -> dict:
        """Analyze the given text to find entities such as patients, illnesses, 
        and fever mentions.

        Args:
            text (str): The text to analyze.

        Returns:
            dict: A dictionary containing the entities found in the text.
        """        
        doc = self.nlp(text)
        entities = {
            'patients': [],
            'illnesses': [],
            'fever_mentions': 0
        }

        # Extract named entities and patterns
        for ent in doc.ents:
            if ent.label_ == 'PERSON':  # Patients
                entities['patients'].append(ent.text)
            elif ent.label_ in ['DISEASE', 'ILLNESS']:  # Illnesses (assumed tags)
                entities['illnesses'].append(ent.text)

        # Count occurrences of 'fever'
        fever_count = text.lower().count('fever')
        entities['fever_mentions'] = fever_count

        return entities
