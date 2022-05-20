from django.db import models

class RegisterModel(models.Model):
	
	name = models.CharField(max_length=100)	
	email = models.EmailField(max_length=100)
	phone = models.IntegerField(max_length=100)
	address = models.CharField(max_length=100)
	tenth =models.IntegerField(max_length=100)
	puc =models.IntegerField(max_length=100)
	degree =models.IntegerField(max_length=100)
	branch =models.CharField(max_length=100)

	def __str__(self):
		return f'{self.name}'

class PredictionModel(models.Model):

	emailid = models.EmailField(max_length=100)
	technical = models.IntegerField(max_length = 100)
	aptitude = models.IntegerField(max_length = 100)
	gd = models.IntegerField(max_length = 100)
	pi = models.IntegerField(max_length = 100)
	tenth = models.IntegerField(max_length = 100)
	puc = models.IntegerField(max_length = 100)
	degree = models.IntegerField(max_length = 100)