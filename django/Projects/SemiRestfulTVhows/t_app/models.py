from django.db import models

class BlogShow(models.Manager):
    def validate_show(self, postData):
         errors = {}
         if len(postData['titleme']) < 5:
             errors["name"] = "Show title must be at least 5 characters"
         if len(postData['network']) < 7:
             errors["desc"] = "the network must be more than 7 characters"
         return errors
         

class Show(models.Model):
    title=models.CharField(default="jenin",  max_length=255)
    network=models.CharField(default='network1',  max_length=255)
    relateddate=models.DateTimeField( auto_now_add=True)
    desc=models.TextField(default="new desription")
    objects=BlogShow()    







    

