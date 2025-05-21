from pydantic import BaseModel

class StudentCreate(BaseModel):
    first_name: str
    last_name: str

class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True