from django.contrib.auth.models import AbstractUser
from django.db import models


class Product(models.Model):
    part_name = models.CharField(max_length=150, verbose_name="Наименование")
    content = models.CharField(max_length=150, verbose_name="Описание")
    photo = models.ImageField(blank=True, verbose_name="Изображение")
    availability = models.IntegerField(verbose_name="Колличество")

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Изделие"
        verbose_name_plural = "Изделия"


class CustomUser(AbstractUser):
    last_login = None
    first_name = None
    last_name = None
    date_joined = None


    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class OrderProduct(models.Model):
    order_id = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name="ID товара")
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE, verbose_name="ID пользователя")
    availability = models.IntegerField(verbose_name="Колличество")

    def __str__(self):
        return f"Заказ {self.pk}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
