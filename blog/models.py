from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class SkewStarh1(models.Model) :
    h1 = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.h1}"

class SkewStarP(models.Model) :
    p = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.p}"

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(help_text="Enter a value between 0 and 100")

    def __str__(self):
        return f"{self.name} - {self.proficiency}%"


class AboutMe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Service(models.Model) :
    image = models.ImageField(upload_to='profile_images/', null=True)
    title = models.CharField(max_length=20)
    subtitle = models.TextField(null=True)

    def __str__(self):
        return self.title
    
class Work(models.Model) :
    number = models.PositiveIntegerField()
    text = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.text
    
class PortfolioTitle(models.Model) :
    title = models.CharField(max_length=20)
    subtitle = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title

class Partfolio(models.Model) :
    image = models.ImageField(upload_to='profile_images/')
    title2 = models.CharField(max_length=50)
    span1 = models.CharField(max_length=20)
    span2 = models.TextField(null=True)
    
    def __str__(self) -> str:
        return self.title2

class BlogTitle(models.Model) :
    title = models.CharField(max_length=20)
    subtitle = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title
    
class Blog(models.Model) :
    image = models.ImageField(upload_to='profile_images/')
    title = models.CharField(max_length=20)
    title2 = models.CharField(max_length=20, null = True)
    text = models.CharField(max_length=255)
    span = models.CharField(max_length=20 ,null=True)
    image2 = models.ImageField(upload_to='profile_imagws/', null=True)
    
    def __str__(self) -> str:
        return self.title
    
class Contact(models.Model) :
    text = models.CharField(max_length=255, null = True)
    adress = models.CharField(max_length=20, null = True)
    phone_number = models.CharField(max_length=17)
    email = models.EmailField()
    facebook = models.CharField(max_length=50, null = True)
    instagram = models.CharField(max_length=50, null = True) 

    def __str__(self) -> str:
        return self.phone_number
    
class BlogSingle(models.Model) :
    image = models.ImageField(upload_to='profile_image/', null = True)
    title = models.CharField(max_length=100, null = True)
    subtitle = models.CharField(max_length=50, null = True) 
    text1 = models.TextField(null = True) 
    text2 = models.TextField(null = True) 
    text3 = models.TextField(null = True) 
    text4 = models.TextField(null = True) 
    text5 = models.TextField(null = True) 
    text6 = models.TextField(null = True)

    def __str__(self) -> str:
        return self.title