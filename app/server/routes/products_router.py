from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

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
def find_all_products():
    try:
        return JSONResponse(status_code=200, content=jsonable_encoder(menu))
    except:
        return {"Error": "COULD NOT COMPLETE THE REQUEST"}
    
@router.get("/{id}", response_description="Return a product per ID")
def find_product_by_id(id: int):
    try:
        for product in menu:
            if product['id'] == id:
                return JSONResponse(status_code=200, content=product)
    except:
        return {"Error": "Could not find product with the given ID"}