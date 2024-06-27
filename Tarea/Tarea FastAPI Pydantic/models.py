from pydantic import BaseModel as BM
from typing import Optional

class Product(BM):
    id:str
    name:str
    price:float
    amount:int

class User(BM):
    id:str
    name:str
    email:str
    age:int
    
class Order(BM):
    id:str
    user_id:str
    product_list:list
    total: Optional[float] = None
    