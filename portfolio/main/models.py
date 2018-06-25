from django.db import models


class Skill(models.Model):
	title = models.TextField()

	class Meta:
		verbose_name = 'Skill'
		verbose_name_plural = "Skills"


class AIProject(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField()

	class Meta:
		verbose_name = 'Ai Project'
		verbose_name_plural = 'AI Projects'


class Contact(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	number = models.CharField(max_length=14)
	message = models.TextField()

	class Meta:
		verbose_name = 'Contact'
		verbose_name_plural = "Contacts"


class Research(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=50)
	slug = models.SlugField()
	description = models.TextField()

	class Meta:
		verbose_name = 'Research'
		verbose_name_plural = 'Researches'
