from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(..., pattern=r'^\d{5}(?:-\d{4})?$')
    country: str

class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    is_active: bool = True
    home_address: Address
    phone: Optional[str] = None

user_data = {
    "user_id": 101,
    "name": " Pinkman",
    "email": "pinkman@example.com",
    "is_active": True,
    "home_address": {
        "street": "nh-8",
        "city": "bbsr",
        "zip_code": "87111",
        "country": "india"
    }
}

try:
    user = User(**user_data)
    
    print("User Model Successfully Validated")
    print(f"User Name: {user.name}")
    print(f"User Email: {user.email}")
    
    print("Nested Address Details")
    print(f"Street: {user.home_address.street}")
    print(f"City: {user.home_address.city}")
    print(f"Zip Code: {user.home_address.zip_code}")
    
except Exception as e:
    print(f"Validation Error: {e}")
    
    
temp=user.model_dump()
print(temp)
print(type(temp))