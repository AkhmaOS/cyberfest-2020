from django.db import models


class CatalogModel(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def __str__(self):
        return self.name
