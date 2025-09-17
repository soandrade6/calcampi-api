from app.utils.constants import AMINO_ACID_MASS

def calculate_molecular_weight(sequence: str) -> float:
    """Calcula el peso molecular de un péptido."""
    total_mass = sum(AMINO_ACID_MASS.get(aa, 0) for aa in sequence)
    total_mass += 18.0152 
    return round(total_mass, 2)
