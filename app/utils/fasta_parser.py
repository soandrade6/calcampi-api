from typing import List

VALID_AMINOACIDS = set("ACDEFGHIKLMNPQRSTVWY")

def parse_fasta(file_content: str) -> List[str]:
    sequences = []
    current_seq = []
    for line in file_content.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if current_seq:
                sequences.append("".join(current_seq))
                current_seq = []
        else:
            if not set(line).issubset(VALID_AMINOACIDS):
                raise ValueError(f"Secuencia inválida: {line}")
            current_seq.append(line)
    if current_seq:
        sequences.append("".join(current_seq))
    return sequences
