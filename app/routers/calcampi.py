from fastapi import APIRouter, UploadFile, File, HTTPException, Body
from typing import Optional
from app.models.request_models import SequenceRequest
from app.utils.fasta_parser import parse_fasta
from app.services.sequence_service import calculate_properties

router = APIRouter()

@router.post("/analyze")
async def analyze_sequence(
    request: Optional[SequenceRequest] = Body(None),
    fasta_file: UploadFile = File(None)
):
    if not request and not fasta_file:
        raise HTTPException(status_code=400, detail="Debe enviar una secuencia o un archivo FASTA")

    results = []

    if request and request.sequence:
        results.append(calculate_properties(request.sequence))

    if fasta_file:
        content = (await fasta_file.read()).decode("utf-8")
        try:
            sequences = parse_fasta(content)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        results.extend([calculate_properties(seq) for seq in sequences])

    return {"results": results}
