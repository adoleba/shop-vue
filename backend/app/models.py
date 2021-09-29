import peewee

from backend.app.database import db

CATEGORIES = (
    ('2in1', '2in1'),
    ('laptop', 'laptop'),
    ('ultrabook', 'ultrabook')
)


class Product(peewee.Model):
    product_id = peewee.IntegerField(primary_key=True)
    producer = peewee.CharField()
    name = peewee.CharField()
    description = peewee.TextField()
    category = peewee.CharField(choices=CATEGORIES)
    memory = peewee.CharField()
    screen = peewee.CharField()
    price = peewee.IntegerField()
    processor = peewee.CharField()
    disk = peewee.CharField()
    onStock = peewee.BooleanField(default=True)
    img_url = peewee.CharField()

    class Meta:
        database = db
