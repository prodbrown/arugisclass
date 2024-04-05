from django.db import models
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Course(models.Model):
	course_name = models.CharField(max_length=255)
	course_code = models.CharField(max_length=255)
	lecture_teacher = models.CharField(max_length=255, blank=True)
	practical_teacher = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.course_name

	def get_absolute_url(self):
		return reverse('dashboard')
#		return reverse('dashboard', args=(str(self.id)))

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	body = RichTextField(null=True, blank=True)
	#body = models.TextField(null=True, blank=True)
	post_date = models.DateField(auto_now_add=True)
	post_image = models.ImageField(null=True, blank=True, upload_to="images/")
	post_file = models.FileField(null=True, blank=True, upload_to="documents/")



	def get_absolute_url(self):
		return reverse('post_detail-view', args=(str(self.id)))


class Notes(models.Model):
	title = models.CharField(max_length=255)
	#body = models.TextField(null=True, blank=True)
	body = RichTextField(null=True, blank=True)
	notes_date = models.DateField(auto_now_add=True)
	course = models.CharField(max_length=300, default='Unknown')
	header_image = models.ImageField(null=True, blank=True, upload_to="images/")
	header_file = models.FileField(null=True, blank=True, upload_to="documents/")


	def get_absolute_url(self):
		return reverse('notes_detail-view', args=(str(self.id)))

