from django.db import models

class Sites(models.Model):
    name = models.CharField('Site name',max_length=30)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    class Meta:
        verbose_name_plural = "Site Names"

class Site(models.Model):
    site_id = models.ForeignKey(Sites, on_delete=models.CASCADE)
    date = models.DateField('Date')
    a_value = models.DecimalField('A Value',max_digits=5, decimal_places=2)
    b_value = models.DecimalField('B Value',max_digits=5, decimal_places=2)
    
    class Meta:
        verbose_name_plural = "Site Items"


