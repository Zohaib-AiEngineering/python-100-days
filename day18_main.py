from fastapi import FastAPI
from pydantic import BaseModel 
app = FastAPI()
List =[]
class Product (BaseModel):
    name: str 
    price: float 
    description: str =None
    in_stock: bool =True
    
@app.get("/products")
def get_all_products():
    return {
        "total_products": len(List),
        "products": List 

    }
@app.post("/products")
def create_product(product: Product):
    product_dict = product.dict()
    List.append(product_dict)
    return {
        "message": "product created sccessfully",
        "product_data": product.dict()
        
    }

