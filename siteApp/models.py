from django.db import models

class Site(models.Model):
     site_name = models.CharField(max_length=200)
     
     def __str__(self):
        return self.site_name 


class SiteDataEntry(models.Model):
    description =  models.CharField(max_length=200)
    A_value = models.FloatField(default=0.00)
    B_value = models.FloatField(default=0.00) 
    date = models.DateField(default=None)
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.description 










