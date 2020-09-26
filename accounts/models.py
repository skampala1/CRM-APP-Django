from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)
	STATUS_L = [
		'Pending', 'Out for delivery', 'Delivered'
	]
	UNITS = [
		{"name": "Ton", 'val': 1000},
		{"name": "Kg", 'val': 1}
	]
	order_name = models.CharField(max_length=200, null=True)
	order_no = models.CharField(max_length=200, null=True)
	company_name = models.CharField(max_length=200, null=True)
	tel_phone = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	contact = models.CharField(max_length=200, null=True)
	product = models.CharField(max_length=200, null=True)
	price = models.CharField(max_length=200, null=True)
	qty = models.CharField(max_length=200, null=True)
	discount = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	#customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True)
	customer_id = models.IntegerField(blank=True, default=0)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


	def __str__(self):
		return str(self.order_name)



	
