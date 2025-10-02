from pydantic import BaseModel,model_validator
class Patient(BaseModel):
    name:str
    age:int



def i_p_data(patient:Patient):
    
        print(patient.name)
        print(patient.age)
        print("inserted into database")
@model_validator(mode='after')
def validate_emergency_contact(cls,model):
    if model.age>60 and 'emergency' not in model.contact_details:
        raise ValueError('Patients older than 60 must have an emergency contact')
    return model
    

def u_p_data(patient:Patient):
   
        print(patient.name)
        print(patient.age)
        print("updated into database")
        
patient_info={'name':"bigya",'age':'90','emergency':'228776'}
patient1=Patient(**patient_info)
u_p_data(patient1)
    