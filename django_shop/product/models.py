from django.db import models

# Create your models here.

class Product(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고')
    registered_dttm = models.DateTimeField(auto_now=True,verbose_name='등록시간')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_table'
        verbose_name='상품'
        verbose_name_plural = '상품'