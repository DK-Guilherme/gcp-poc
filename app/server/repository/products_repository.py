from app.server.config.database import products_collection

def get_all_products():
    try:
        products_from_db = products_collection.find({}, {'_id': False})
        products_list = list(products_from_db)
        return products_list
    except () as e:
        print(e)
        return e