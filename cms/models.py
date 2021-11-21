from django.db import models

# Create your models here.
class CmsSlider(models.Model):
	cms_img = models.ImageField(upload_to='slider/img/')
	cms_title = models.CharField(max_length=100, verbose_name='Заголовок')
	cms_text = models.CharField(max_length=100, verbose_name='Текст')

	def __str__(self):
		return self.cms_title

	class Meta:
		verbose_name = 'Слайд'
		verbose_name_plural = 'Слайды'