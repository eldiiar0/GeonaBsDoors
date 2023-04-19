from django.db import models
from datetime import date
import os 


def image_upload_path(instance, filename):
	# Get the file extension of the uploaded file
	extension = os.path.splitext(filename)[-1]
	# Construct a new filename for the file
	today = date.today()
	try:
		new_filename = f"{instance.title}_{today.strftime('%Y-%m-%d').replace(' ', '_')}{extension}"
	except:
		new_filename = f"{instance.doortype.title + instance.cover}_{today.strftime('%Y-%m-%d').replace(' ', '_')}{extension}"
	# Return the new file path
	return os.path.join('media/', new_filename)


def news_image_upload(instance, filename):
	# Get the file extension of the uploaded file
	extension = os.path.splitext(filename)[-1]
	# Construct a new filename for the file
	today = date.today()
	new_filename = f"{instance.title}_{today.strftime('%Y-%m-%d').replace(' ', '_')}{extension}"
	# Return the new file path
	return os.path.join('media/news/', new_filename)


class Category(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to=image_upload_path)
	description = models.TextField(blank=True) 

	def __str__(self):
		return self.title


class SubCategory(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE) 
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to=image_upload_path) 
	description = models.TextField(blank=True) 

	def __str__(self):
		return self.title


class DoorType(models.Model):
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
	collection = models.CharField(max_length=255) 
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.title


class Door(models.Model):
	doortype = models.ForeignKey(DoorType, on_delete=models.CASCADE)
	cover = models.CharField(max_length=255)
	color_canvas = models.CharField(max_length=255)
	color_patina = models.CharField(max_length=255, blank=True)
	image = models.ImageField(upload_to=image_upload_path, blank=True)
	glazing = models.CharField(max_length=255, blank=True)
	width = models.CharField(max_length=255, blank=True)
	height = models.CharField(max_length=255, blank=True) 
	thickness = models.CharField(max_length=255, blank=True)
	mouldings = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return ', '.join([self.doortype.title, self.color_canvas, self.glazing]) 


class News(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to=news_image_upload)
	extra_img1 = models.ImageField(upload_to=news_image_upload, blank=True)
	extra_img2 = models.ImageField(upload_to=news_image_upload, blank=True)
	extra_img3 = models.ImageField(upload_to=news_image_upload, blank=True)
	date = models.DateField()
	description = models.TextField(blank=True) 

	def __str__(self):
		return self.title


class Message(models.Model):
	name = models.CharField(max_length=255)
	phone = models.CharField(max_length=20)
	city = models.CharField(max_length=50)
	emai = models.EmailField()
	text_message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		self.msg_date = str(self.date)
		return ', '.join([self.name, self.phone, self.msg_date[:20] ]) 
