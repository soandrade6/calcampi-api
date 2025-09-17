from app.utils.constants import IB_SCALE

def calculate_IB_index(sequence: str) -> float:
    """Calcula el índice de Boman (IB)."""
    if not sequence:
        return 0.0
    value = -(sum(IB_SCALE.get(aa, 0) for aa in sequence) / len(sequence))
    return round(value, 2)


def calculate_IA_index(sequence: str) -> float:
    """Calcula el índice de alifaticidad (IA)."""
    length = len(sequence)
    if length == 0:
        return 0.0

    A = sequence.count("A") / length * 100
    V = sequence.count("V") / length * 100
    I = sequence.count("I") / length * 100
    L = sequence.count("L") / length * 100

    IA = A + (2.9 * V) + (3.9 * (I + L))
    return round(IA, 2)
