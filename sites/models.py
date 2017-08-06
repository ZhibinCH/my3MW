from django.db import models

#class Sites(models.Model):
#    site_name = models.CharField(max_length=30)
#    site_id = models.CharField(max_length=30)
#    date = models.DateTimeField()
#    a_value = models.DecimalField(max_digits=5, decimal_places=2)
#    b_value = models.DecimalField(max_digits=5, decimal_places=2)

class Sites(models.Model):
    name = models.CharField(max_length=30)


