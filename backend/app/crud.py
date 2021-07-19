from backend.app import models, schemas


def get_products(skip: int = 0, limit: int = 100):
    return list(models.Product.select().offset(skip).limit(limit))


def create_product(product):
    db_product = models.Product(
        producer=product['producer'],
        name=product['name'],
        description=product['description'],
        category=product['category'],
        memory=product['memory'],
        screen=product['screen'],
        price=product['price'],
        processor=product['processor'],
        disk=product['disk'],
    )
    db_product.save()
    return db_product


def update_product(product_id: int, product_data: schemas.Product):
    product = models.Product.filter(models.Product.id == product_id).first()
    product.producer = product_data.producer
    product.name = product_data.name
    product.description = product_data.description
    product.category = product_data.category
    product.memory = product_data.memory
    product.screen = product_data.screen
    product.price = product_data.price
    product.processor = product_data.processor
    product.disk = product_data.disk
    product.onStock = product_data.onStock
    product.save()
    return product


def delete_product(product_id: int):
    return models.Product.delete().where(models.Product.id == product_id).execute()


def get_product(product_id: int):
    return models.Product.filter(models.Product.id == product_id).first()
