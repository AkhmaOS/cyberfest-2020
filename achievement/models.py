from django.db import models

class AchievementModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)
    progress = models.CharField(max_length=255)
    kirgu_point = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.name