def i_p_data(name:str,age:int):
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print("inserted into database")
    else:
     raise TypeError("incorrect data type")



def u_p_data(name:str,age:int):
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print("updated into database")
    else:
     raise TypeError("incorrect data type")
