from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
 name: str
 email: EmailStr
 age: int
 weight: float
 height: float
 married: bool
 allergies: List[str]
 contact_details: Dict[str, str]

 @computed_field
 @property
 def bmi(self) -> float:
   bmi = round(self.weight/(self.height**2),2)
   return bmi

def update_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print(patient.allergies)
  print(patient.married)
  print('BMI', patient.bmi)
  print('Updated')

if __name__ == "__main__":
  patient_info = {
    'name': 'Prem',
    'email': 'abc@hdfc.com',
    'linkedin_url': 'http://linkedin.com/1322',
    'age': '65',
    'weight': '75.8',
    'height': '1.76',
    'married': False,
    'allergies': ['Peanuts', 'Dust'],
    'contact_details': {'number': '8627048480', 'emergency': '328497324'}
  }
  patient1 = Patient(**patient_info)
  
  update_patient_data(patient1)
