from pydantic import BaseModel 

class Address(BaseModel):

  city: str
  state: str
  pin: str

class Patient(BaseModel):

  name: str
  gender: str
  age: int
  address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'prem', 'gender': 'male', 'age': 20, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude={'address': ['state']})
print(temp)
print(type(temp))