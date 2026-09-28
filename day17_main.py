from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello! My first FastAPI app"}
@app.get ("/about")
def about():
    return {"message": "This is my FastAPI learning project"}

@app.get("/products")
def products():
    return {
        "products": [
            "Laptop",
            "Keyboard",
            "Mouse"
        ]
    }
@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id}
@app.get("/search")
def search_products(category: str, limit: int):
    return {
        "category": category,
        "limit": limit
    }