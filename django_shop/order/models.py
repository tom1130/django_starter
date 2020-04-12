from django.db import models

# Create your models here.

class Order(models.Model):
    objects = models.Manager()
    User = models.ForeignKey('user.User',on_delete=models.CASCADE,verbose_name='사용자')
    Product = models.ForeignKey('product.Product',on_delete=models.CASCADE,verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    registered_dttm = models.DateTimeField(auto_now=True,verbose_name='등록날짜')


    def __str__(self):
        return str(self.User) + ' ' + str(self.Product)
    
    class Meta:
        db_table = 'order_table'
        verbose_name='주문'
        verbose_name_plural = '주문'