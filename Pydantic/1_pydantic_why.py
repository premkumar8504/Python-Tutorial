from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
  name: Annotated[str, Field(max_length=50, title='Name of the Patient', description='Give the name of the patient is less than 50 chars', examples=['Prem', 'Nitish'])]
  email: EmailStr
  linkedin_url: AnyUrl
  age: int = Field(gt=0, lt=30)
  weight: Annotated[float, Field(gt=0, strict=True)]
  married: Annotated[bool, Field(default=False, description='Is the patient married or not')]
  allergies: Annotated[Optional[list[str]], Field(default=None, max_length=5)]
  contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
  print(patient.name)
  print(patient.email)
  print(patient.age)
  print('Inserted')

def update_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print(patient.allergies)
  print(patient.married)
  print('Updated')

if __name__ == "__main__":
  patient_info = {
    'name': 'Prem',
    'email': 'abc@gmail.com',
    'linkedin_url': 'http://linkedin.com/1322',
    'age': 20,
    'weight': 75.8,
    'married': False,
    'allergies': ['Peanuts', 'Dust'],
    'contact_details': {'number': '8627048480'}
  }
  patient1 = Patient(**patient_info)
  
  update_patient_data(patient1)
