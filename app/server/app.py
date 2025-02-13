from fastapi import FastAPI
from app.server.routes.products_router import router as ProductsRouter


app = FastAPI()

@app.get("/hello")
def hello_world():
    return {"Hello": "World"}

app.include_router(ProductsRouter, tags=["Products"], prefix="/products")