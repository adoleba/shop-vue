from typing import List

from fastapi import FastAPI, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from . import crud, database, models, schemas
from .database import db_state_default

database.db.connect()
database.db.create_tables([models.Product])
database.db.close()

app = FastAPI(title="VueShop Api")


async def reset_db_state():
    database.db._state._state.set(db_state_default.copy())
    database.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        database.db.connect()
        yield
    finally:
        if not database.db.is_closed():
            database.db.close()


@app.post(
    "/products/",
    response_model=schemas.Product,
    dependencies=[Depends(get_db)],
    tags=["products"],
    summary="Add a new product"
)
def create_product(product: schemas.Product):
    return crud.create_product(product=product)


@app.get(
    "/products/",
    response_model=List[schemas.Product],
    dependencies=[Depends(get_db)],
    tags=["products"],
    summary="View list of all products"
)
def read_products():
    products = crud.get_products()
    return products


@app.put(
    "/products/{product_id}",
    response_model=schemas.Product,
    dependencies=[Depends(get_db)],
    tags=["products"],
    summary="Update existing product"
)
def update_product(product_id: int, product_data: schemas.Product):
    updated_product = crud.update_product(product_id, product_data)
    return updated_product


@app.delete(
    "/products/{product_id}",
    tags=["products"],
    summary="Delete product"
)
def delete_product(product_id: int):
    db_product = crud.delete_product(product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted"}


@app.get(
    "/products/{product_id}",
    response_model=schemas.Product,
    dependencies=[Depends(get_db)],
    tags=["products"],
    summary="View product with given id"
)
def read_product(product_id: int):
    db_product = crud.get_product(product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
