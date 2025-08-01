from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
 name: str
 email: EmailStr
 age: int
 weight: float
 married: bool
 allergies: List[str]
 contact_details: Dict[str, str]

 @model_validator(mode='after')
 def validate_emergency_contact(cls, model):
   if model.age > 60 and 'emergency' not in model.contact_details:
     raise ValueError('Patient older than 60 must have emergency contact')
   return model


def update_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print(patient.allergies)
  print(patient.married)
  print('Updated')

if __name__ == "__main__":
  patient_info = {
    'name': 'Prem',
    'email': 'abc@hdfc.com',
    'linkedin_url': 'http://linkedin.com/1322',
    'age': '65',
    'weight': '75.8',
    'married': False,
    'allergies': ['Peanuts', 'Dust'],
    'contact_details': {'number': '8627048480', 'emergency': '328497324'}
  }
  patient1 = Patient(**patient_info)
  
  update_patient_data(patient1)
