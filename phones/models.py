from django.db import models

MAX_LEN = 255


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(
        max_length=MAX_LEN
    )
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(
        max_length=MAX_LEN
    )

    def __str__(self):
        return f'Название:{self.name}, Цена:{self.price},{self.image}, Дата:{self.release_date}, LTE:{self.lte_exists}, Slug:{self.slug}'
