from django.db import models

# Create your models here.
#pet model
class Pet(models.Model): 
    name = models.CharField(max_length=100) 
    age = models.IntegerField() 
    available = models.BooleanField(default=True) 
    image = models.ImageField(upload_to='images/', null=True) 
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True) 
    def __str__(self): 
        return self.name

#user model
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

#order model
class Order(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.pet.name + ' - ' + self.user.username

#如此類推，每一個 model 都需要一個 class 來定義        
