from backend.app import models, schemas


def get_products(skip: int = 0, limit: int = 100):
    return list(models.Product.select().offset(skip).limit(limit))


def create_product(product: schemas.Product):
    db_product = models.Product(
        producer=product.producer,
        name=product.name,
        description=product.description,
        category=product.category,
        memory=product.memory,
        screen=product.screen,
        price=product.price,
        processor=product.processor,
        disk=product.disk,
        onStock=product.onStock
    )
    db_product.save()
    return db_product


def get_product(product_id: int):
    return models.Product.filter(models.Product.id == product_id).first()
