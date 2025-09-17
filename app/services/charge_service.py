from app.utils.constants import PKA_VALUES

def calculate_net_charge(sequence: str, pH: float = 7.0) -> float:
    """Calcula la carga neta de un péptido a un pH dado (default=7)."""
    positive, negative = 0.0, 0.0

    for aa in sequence:
        if aa in ["R", "K", "H"]:
            positive += (10**PKA_VALUES[aa]) / (10**pH + 10**PKA_VALUES[aa])
        elif aa in ["D", "E", "C", "Y"]:
            negative += (10**pH) / (10**pH + 10**PKA_VALUES[aa])

    positive += (10**PKA_VALUES["Nterm"]) / (10**pH + 10**PKA_VALUES["Nterm"])
    negative += (10**pH) / (10**pH + 10**PKA_VALUES["Cterm"])

    return round(positive - negative, 1)



