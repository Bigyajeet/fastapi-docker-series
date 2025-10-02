from pydantic import BaseModel
from typing import List,Dict,Optional
class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool
    allergies:Optional[List[str]]=None
    c_details:Dict[str,str]



def i_p_data(patient:Patient):
    
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.c_details)
        print("inserted into database")
    

def u_p_data(patient:Patient):
   
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.c_details)
        print("updated into database")
        
patient_info={'name':"bigya",'age':30,"weight":66.5,'married':False,'allergies':['pollen','dust'],'c_details':{'email':'bigya@gmail.com','phone':'9665565454'}}
patient1=Patient(**patient_info)
u_p_data(patient1)
    