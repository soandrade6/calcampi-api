from typing import Dict
from app.services.molecular_service import calculate_molecular_weight
from app.services.charge_service import calculate_net_charge
from app.services.isoelectric_point_service import calculate_isoelectric_point
from app.services.hydrophobicity_service import calculate_hydrophobicity, calculate_hydrophobic_percent
from app.services.index_service import calculate_IB_index, calculate_IA_index
from app.services.structure_service import calculate_structural_trend


def calculate_properties(sequence: str) -> Dict:
    """Orquesta todos los cálculos de propiedades para un péptido."""
    return {
        "sequence": sequence,
        "length": len(sequence),
        "molecular_weight": calculate_molecular_weight(sequence),
        "net_charge": calculate_net_charge(sequence, pH=7.0),
        "hydrophobicity": calculate_hydrophobicity(sequence),
        "IB_index": calculate_IB_index(sequence),
        "IA_index": calculate_IA_index(sequence),
        "isoelectric_point": calculate_isoelectric_point(sequence),
        "hydrophobic_percent": calculate_hydrophobic_percent(sequence),
        "structural_trend": calculate_structural_trend(sequence),
    }
