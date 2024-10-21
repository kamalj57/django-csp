from django.db import models
from django_quill.fields import QuillField




class QuillPost(models.Model):
    content = QuillField()
    
    
class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.CharField(max_length=10)
    salary=models.CharField(max_length=10000)
    

class Blog(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    is_draft=models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.title


class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=35)
    
    def __str__(self):
        return self.name
    
    

class NBlogs(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.CharField(max_length=35,blank=True,default='kamalesh')
    pub_date=models.DateField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    sub_category=models.CharField(max_length=100,blank=True)
    readtime=models.IntegerField()
    
    def __str__(self):
        return self.title
    
    
from colorfield.fields import ColorField
from django.db import models

class MyModel(models.Model):
    color = ColorField(default='#FF0000')