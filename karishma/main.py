from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
class Product(BaseModel):
    name: str
    description: str
    price: float
    gst: float

app = FastAPI()

@app.post('/calculate_tax')
def calculate_tax(product: Product):
    total_bill = product.price + product.gst
    return {
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'gst': product.gst,
        'total_bill': total_bill
}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)