from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Marca = models.CharField(max_length=200)
    Modelo = models.CharField(max_length=200, default='')
    Año = models.IntegerField(default=0)
    Color = models.CharField(max_length=200, default='')
    Num_Puertas = models.IntegerField(default=0)
    Descripción = models.TextField()
    Precio = models.IntegerField(default=0)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Marca