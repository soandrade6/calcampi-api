from typing import Optional, Annotated
from pydantic import BaseModel, constr

class SequenceRequest(BaseModel):
    sequence: Optional[
        Annotated[str, constr(pattern=r'^[ACDEFGHIKLMNPQRSTVWY]+$')]
    ] = None
