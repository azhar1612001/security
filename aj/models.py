from django.db import models

# Create your models here.
class BookingDetail(models.Model):
	name=models.CharField(max_length=50)
	phone=models.IntegerField()
	address=models.CharField(max_length=100)
	city=models.CharField(max_length=20)
	state=models.CharField(max_length=20)
	pin_code=models.IntegerField()
	date=models.DateField()
	message=models.CharField(max_length=300,default="nothing")

	def __str__(self):
		return self.name

class User(models.Model):
	pass