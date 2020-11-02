from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('yeararchive', kwargs={'pk': self.pk})

#class TemplateviewArticle(models.Model):
 #   title = models.CharField(max_length=200)

  #  updated_on = models.DateTimeField(auto_now= True)
   # content = models.TextField()


    #def get_absolute_url(self):
     #   return reverse('tempview', kwargs={'pk': self.pk})

#class defaultemplate(models.Model):
 #   title=models.CharField(max_length=200)
  #  pub_date= models.DateField()
   # updated_on = models.DateTimeField(auto_now= True)

#class TemplateviewArticledefaultemplate(models.Model):
 #   title=models.CharField(max_length=200)