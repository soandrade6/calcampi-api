def calculate_structural_trend(sequence: str) -> str:
    """Estima la tendencia secundaria (hélice, lámina, coil)."""
    helix = sum(aa in ['A','L','M','Q','E','H','K','R'] for aa in sequence)
    sheet = sum(aa in ['I','W','F','V','Y','T','C'] for aa in sequence)
    coil  = sum(aa in ['P','S','G','N','D'] for aa in sequence)

    length = len(sequence)
    helix, sheet, coil = (round((x/length)*100,1) for x in (helix, sheet, coil))

    if helix > sheet and helix > coil:
        prediction = "Posiblemente Alfa Hélice"
    elif sheet > helix and sheet > coil:
        prediction = "Posiblemente Lámina B"
    else:
        prediction = "No tendencia dominante"

    return f"%Hélice: {helix}  %Lámina: {sheet}  %Coil: {coil} --> {prediction}"
