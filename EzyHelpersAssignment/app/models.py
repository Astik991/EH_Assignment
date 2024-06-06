from django.db import models

class Helper(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    skill = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    helper = models.OneToOneField(Helper, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.helper} assigned to {self.customer}"
