from app.services.charge_service import calculate_net_charge

def calculate_isoelectric_point(sequence: str) -> float:
    """Calcula el punto isoeléctrico mediante barrido de pH."""
    for pH in [x / 100 for x in range(0, 1401)]:
        if -0.1 <= calculate_net_charge(sequence, pH) <= 0.1:
            return round(pH, 1)
    return 0.0