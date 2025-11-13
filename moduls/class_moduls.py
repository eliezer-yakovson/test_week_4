from pydantic import BaseModel


class CaesarRequest(BaseModel):
    text: str
    offset: int
    mode: str

class FenceDecryptRequest(BaseModel):
    text: str