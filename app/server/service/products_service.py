from app.server.repository.products_repository import (
    get_all_products
)

def find_all_products():
    product_db = get_all_products()
    return product_db
