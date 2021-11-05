from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class basicsiteinfo(models.Model):
  sitetitle = models.CharField(("site title"), max_length=50)
  email = models.EmailField(("Email"), max_length=254)
  phone = models.CharField(("phone"), max_length=50)
  headertitle = models.CharField(("LinkTitle"), max_length=100, default="")
  headerlink = models.CharField(("Link"), max_length=255, default="")
 

class contact(models.Model):
  name = models.CharField(("name"), max_length=50)
  email = models.EmailField(("name"), max_length=50)
  message = models.TextField(("message"))

  def __str__(self):
      return self.name
  


