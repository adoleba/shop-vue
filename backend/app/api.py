from typing import List

from fastapi import FastAPI, Depends, HTTPException

from . import crud, database, models, schemas
from .database import db_state_default

database.db.connect()
database.db.create_tables([models.Product])
database.db.close()

app = FastAPI()


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


@app.post("/products/", response_model=schemas.Product, dependencies=[Depends(get_db)],)
def create_product(product: schemas.Product):
    return crud.create_product(product=product)


@app.get("/products/", response_model=List[schemas.Product], dependencies=[Depends(get_db)])
def read_products():
    products = crud.get_products()
    return products


@app.get("/products/{product_id}", response_model=schemas.Product, dependencies=[Depends(get_db)])
def read_product(product_id: int):
    db_product = crud.get_product(product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
