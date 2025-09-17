from app.utils.constants import HYDROPHOBICITY_SCALE, HYDROPHOBIC

def calculate_hydrophobicity(sequence: str) -> str:
    """Calcula la hidrofobicidad promedio del péptido."""
    if not sequence:
        return "0.00 -> Secuencia vacía"
    avg = sum(HYDROPHOBICITY_SCALE.get(aa, 0) for aa in sequence) / len(sequence)
    avg = round(avg, 2)
    return f"{avg} -> {'Hidrofóbico' if avg >= 0 else 'Hidrofílico'}"


def calculate_hydrophobic_percent(sequence: str) -> float:
    """Porcentaje de aminoácidos hidrofóbicos en el péptido."""
    if not sequence:
        return 0.0
    count = sum(1 for aa in sequence if aa in HYDROPHOBIC)
    return round((count / len(sequence)) * 100, 2)
