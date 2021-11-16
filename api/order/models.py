from django.db import models
from django.contrib.auth import get_user_model
from api.jewelry.models import Jewelry

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="order_Jewelry")
    jewelry = models.ManyToManyField(Jewelry)
    ordered_date = models.DateField(auto_now=True)