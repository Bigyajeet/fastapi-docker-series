from pydantic import BaseModel,field_validator
from typing import List,Dict,Optional
class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool
    allergies:Optional[List[str]]=None
    c_details:Dict[str,str]

@field_validator('email')
@classmethod
def e_validator(cls,value):
    valid_domain=["hdfc.com",'icic.com']
    #abc@gmail.com
    domain_name=value.split('@')[-1]
    if domain_name not in valid_domain:
        raise ValueError("Not a valid domain")
    return value


@field_validator('age',mode='after')
@classmethod
def validate_age(cls,value):
    if 0<value<100:
        return value
    else:
        raise ValueError('Age shouldd be in between 0 amd 100') 


def i_p_data(patient:Patient):
    
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.c_details)
        print("inserted into database")
        
        

@field_validator('name')
@classmethod
def t_name(cls,value):
    return value.upper()



def u_p_data(patient:Patient):
   
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.c_details)
        print("updated into database")
        
patient_info={'name':"bigya",'age':30,"weight":66.5,'married':False,'allergies':['pollen','dust'],'c_details':{'email':'bigya@icic.com','phone':'9665565454'}}
patient1=Patient(**patient_info)
u_p_data(patient1)
    