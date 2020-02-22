from django.db import models


class RatingModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    rating_spot = models.CharField(max_length=255)
    kirgu_point = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return self.name
