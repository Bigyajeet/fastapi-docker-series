from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    height: float
    email: EmailStr
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    c_details: Dict[str, str]
    
    @computed_field
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi

def u_p_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('bmi', patient.bmi)
    print("updated into database")

patient_info = {
    'name': "bigya",
    'age': 30,
    'height': 1.75,
    'weight': 66.5,
    'email': 'bigya@icic.com',
    'married': False,
    'allergies': ['pollen','dust'],
    'c_details': {'phone':'9665565454'}
}

patient1 = Patient(**patient_info)
u_p_data(patient1)