import shutil
from enum import Enum
from typing import List

from fastapi import FastAPI, Depends, HTTPException, Form, UploadFile, File
from starlette.middleware.cors import CORSMiddleware

from . import crud, database, models, schemas
from .database import db_state_default

database.db.connect()
database.db.create_tables([models.Product])
database.db.close()

app = FastAPI(title="VueShop Api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ProductCategories(str, Enum):
    _2in1 = '2in1'
    laptop = 'laptop'
    ultrabook = 'ultrabook'


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
    "/api/products/",
    dependencies=[Depends(get_db)],
    tags=["products"],
    summary="Add a new product"
)
def create_product(category: ProductCategories = ProductCategories.laptop,
                   producer: str = Form(..., min_length=2),
                   name: str = Form(..., min_length=2),
                   description: str = Form(..., min_length=20),
                   memory: str = Form(..., min_length=2),
                   screen: str = Form(..., min_length=2),
                   price: int = Form(..., gt=0),
                   processor: str = Form(..., min_length=2),
                   disk: str = Form(..., min_length=2),
                   on_stock: bool = Form('true'),
                   img_url: UploadFile = File(...)):

    with open('../public/media/'+img_url.filename, 'wb') as image:
        shutil.copyfileobj(img_url.file, image)

    img_url = str('media/'+img_url.filename)

    product = {'producer': producer, 'name': name, 'description': description, 'category': category.value, 'memory': memory,
               'screen': screen, 'price': price, 'processor': processor, 'disk': disk, 'on_stock': on_stock,
               'img_url': img_url}
    return crud.create_product(product=product)


@app.get(
    "/api/products/",
    response_model=List[schemas.Product],
    dependencies=[Depends(get_db)],
    tags=["products"],
    summary="View list of all products"
)
def read_products():
    products = crud.get_products()
    return products


@app.put(
    "/api/products/{product_id}",
    dependencies=[Depends(get_db)],
    tags=["products"],
    summary="Update existing product"
)
def update_product(product_id: int,
                   category: ProductCategories = ProductCategories.laptop,
                   producer: str = Form(..., min_length=2),
                   name: str = Form(..., min_length=2),
                   description: str = Form(..., min_length=20),
                   memory: str = Form(..., min_length=2),
                   screen: str = Form(..., min_length=2),
                   price: int = Form(..., gt=0),
                   processor: str = Form(..., min_length=2),
                   disk: str = Form(..., min_length=2),
                   on_stock: bool = Form('true'),
                   img_url: UploadFile = File(...)):

    with open('../public/media/'+img_url.filename, 'wb') as image:
        shutil.copyfileobj(img_url.file, image)

    img_url = str('media/'+img_url.filename)

    product_data = {'producer': producer, 'name': name, 'description': description, 'category': category.value, 'memory': memory,
                    'screen': screen, 'price': price, 'processor': processor, 'disk': disk, 'on_stock': on_stock,
                    'img_url': img_url}
    updated_product = crud.update_product(product_id, product_data=product_data)
    return updated_product


@app.delete(
    "/api/products/{product_id}",
    tags=["products"],
    summary="Delete product"
)
def delete_product(product_id: int):
    db_product = crud.delete_product(product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted"}


@app.get(
    "/api/products/{product_id}",
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

