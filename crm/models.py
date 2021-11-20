from django.db import models

# Create your models here.
class Order(models.Model):
	order_bd = models.DateTimeField(auto_now=True)
	order_name = models.CharField(max_length=100, verbose_name="Имя")
	order_phone = models.CharField(max_length=100, verbose_name="Телефон")

	def __str__(self):
		return self.order_name

	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'