from typing import Dict

def calculate_properties(sequence: str) -> Dict:
    length = len(sequence)
    return {
        "sequence": sequence,
        "length": length,
        "molecular_weight": length * 110,  # mock simplificado
        "hydrophobicity": 42.86,           # mock
        "charge": 0,                       # mock
        "isoelectric_point": 7.0           # mock
    }
