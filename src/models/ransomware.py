from pydantic import BaseModel

class Ransomware(BaseModel):
  private_key: str
  public_key: str