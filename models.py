from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=80)
    username = models.CharField(max_length=80,primary_key=True)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    confirmpassword = models.CharField(max_length=40)
    status = models.CharField(max_length=10,default='U')


    def __str__(self):
        return self.username

#file upload class
class Post(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,primary_key=True)
    file_field = models.FileField(upload_to='images/')
    desc = models.TextField()

    def __str__(self):
        return f'{self.username}=> {self.title}'    

#favorites class
class Wishlist(models.Model):
    username = models.ForeignKey(Customer,on_delete=models.CASCADE)
    title = models.ForeignKey(Post,on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    added_date = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return f'{self.username}=> {self.title}' 


#review or rating of a document
class review(models.Model):
    username = models.ForeignKey(Customer,on_delete=models.CASCADE)
    title = models.ForeignKey(Post,on_delete=models.CASCADE)
    review_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=4000)