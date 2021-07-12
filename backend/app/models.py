import peewee

from backend.app.database import db

CATEGORIES = (
    ('2in1', '2in1'),
    ('laptop', 'laptop'),
    ('ultrabook', 'ultrabook')
)


class Product(peewee.Model):
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

    class Meta:
        database = db
