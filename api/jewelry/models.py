from decimal import Decimal
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only letters.')

class Jewelry(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='Title', db_index=True, max_length=50, default='', null=False, blank=False, validators=[alphanumeric] )
    date = models.DateField(verbose_name='Date', db_index=True, max_length=10)
    JEW_TYPES_TYPE =(
        (1, 'Rings'),
        (2, 'Earrings'),
        (3, 'Bracelets'),
    )
    jew_types = models.IntegerField(verbose_name='Types', choices=JEW_TYPES_TYPE)
    JEW_MATER_TYPE = (
        (1, 'Gold'),
        (2, 'Silver'),
        (3, 'Platinum'),
    )
    jew_mat = models.IntegerField(verbose_name='Materials', choices=JEW_MATER_TYPE)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return self.title


