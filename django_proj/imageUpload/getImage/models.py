from django.db import models

# Create your models here.
class image(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    title = models.CharField(max_length=100)
    filepath = models.ImageField(upload_to='images',null=True,verbose_name=None)
    description = models.CharField(max_length=500)
    datetime = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.name + ": " + str(self.imagefile)