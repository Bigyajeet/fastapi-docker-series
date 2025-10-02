from pydantic import BaseModel
class Patient(BaseModel):
    name:str
    age:int



def i_p_data(patient:Patient):
    
        print(patient.name)
        print(patient.age)
        print("inserted into database")
    

def u_p_data(patient:Patient):
   
        print(patient.name)
        print(patient.age)
        print("updated into database")
        
patient_info={'name':"bigya",'age':30}
patient1=Patient(**patient_info)
u_p_data(patient1)
    