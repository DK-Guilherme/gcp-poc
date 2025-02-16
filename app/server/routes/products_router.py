from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.server.service.products_service import (
    find_all_products
)

router = APIRouter()

menu = [
    {   'id': 1,
        'name': 'coffee',
        'price': 2.5
     },
    {
        'id': 2,
        'name': 'cake',
        'price': 10
    },
    {
        'id': 3,
        'name': 'tea',
        'price': 3.2
    },
    {
        'id': 4,
        'name': 'croissant',
        'price': 5.79
    }
]

@router.get("", response_description="Return all products")
def getall_products():
    try:
        products = find_all_products()
        print(products)
        return JSONResponse(status_code=200, content=jsonable_encoder(products))
    except () as e:
        print(e)
        return {"Error": f"COULD NOT COMPLETE THE REQUEST"}
    
@router.get("/{id}", response_description="Return a product per ID")
def find_product_by_id(id: int):
    try:
        for product in menu:
            if product['id'] == id:
                return JSONResponse(status_code=200, content=product)
    except () as e:
        return {"Error": "Could not find product with the given ID"}