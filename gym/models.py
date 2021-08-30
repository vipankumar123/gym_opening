from django.db import models

# Create your models here.

class Enquiry(models.Model):
	name = models.CharField(max_length=100)	
	contact = models.CharField(max_length=100)
	emailid = models.CharField(max_length=100)
	age = models.IntegerField()
	gender = models.CharField(max_length=100)


	def __str__(self):
		return self.name


class Equipment(models.Model):
	name = models.CharField(max_length=100)	
	price = models.CharField(max_length=100)
	unit = models.CharField(max_length=100)
	date = models.CharField(max_length=100)
	description = models.CharField(max_length=100)


	def __str__(self):
		return self.name

class Plan(models.Model):
	name = models.CharField(max_length=100)	
	amount = models.CharField(max_length=100)
	duration = models.CharField(max_length=100)


	def __str__(self):
		return self.name		

class Member(models.Model):
	name = models.CharField(max_length=50)	
	contact = models.CharField(max_length=10)
	emailid = models.CharField(max_length=100)
	age = models.CharField(max_length=110)	
	gender = models.CharField(max_length=20)
	plan = models.CharField(max_length=50)
	joindate = models.CharField(max_length=40)
	expiredate = models.CharField(max_length=40)
	initialamount = models.CharField(max_length=10)


	def __str__(self):
		return self.name		















