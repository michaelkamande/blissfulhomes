from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


types = (
	('Appartement', 'Appartement'),
	('Maison', 'Maison'),
	('Bureau', 'Bureau'),
	('Terrain', 'Terrain'),
	)

classification = (
	('A Louer', 'A Louer'),
	('A Vendre', 'A Vendre'),
	)

disponibility = (
	('Disponible', 'Disponible'),
	('Déjà pris', 'Déjà pris'),
	)

boolean = (
	('Oui', 'Oui'),
	('Non', 'Non'),
	)


class Properties(models.Model):
	titre = models.CharField(max_length=100)
	category = models.CharField(max_length=20, choices=types)
	mode = models.CharField(max_length=20, choices=classification)
	salon = models.IntegerField(default=1)
	chambres = models.IntegerField(default=1)
	salle_de_bain = models.IntegerField(default=1)
	cuisine = models.CharField(max_length=3, choices=boolean)
	parking = models.CharField(max_length=3, choices=boolean)
	description = models.TextField(blank=True, null=True)
	prix = models.CharField(max_length=20)
	zone = models.CharField(max_length=100)
	ville = models.CharField(max_length=100)
	est_disponible = models.CharField(max_length=20, choices=disponibility, default='Disponible')
	publicateur = models.CharField(max_length=100)
	contact = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'properties')
	image1 = models.ImageField(blank=True, null=True, upload_to = 'properties')
	image2 = models.ImageField(blank=True, null=True, upload_to = 'properties')
	image3 = models.ImageField(blank=True, null=True, upload_to = 'properties')
	image4 = models.ImageField(blank=True, null=True, upload_to = 'properties')
	image5 = models.ImageField(blank=True, null=True, upload_to = 'properties')
	image6 = models.ImageField(blank=True, null=True, upload_to = 'properties')
	image7 = models.ImageField(blank=True, null=True, upload_to = 'properties')
	image8 = models.ImageField(blank=True, null=True, upload_to = 'properties')
	image9 = models.ImageField(blank=True, null=True, upload_to = 'properties')
	favoris = models.ManyToManyField(User, related_name='favoris', blank=True)
	publier = models.BooleanField(default=False)


	def __str__(self):
		return str(self.titre) + ' ' + str(self.mode) + ' ' + str(self.zone)

	def get_absolute_url(self):
		return reverse('property', kwargs = {'id': self.id})

	@property
	def imageURL(self):
		try:
			url = self.image.url

		except:
			url = ''
		return url

	def save(self, *args, **kwargs):
		super(Properties, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 360 or img.width > 640:
			output_size = (640, 360)
			img.thumbnail(output_size)
			img.save(self.image.path)

	@property
	def image1URL(self):
		try:
			url = self.image1.url

		except:
			url = ''
		return url

	def save1(self, *args, **kwargs):
		super(Properties, self).save(*args, **kwargs)

		img = Image.open(self.image1.path)

		if img.height > 360 or img.width > 640:
			output_size = (640, 360)
			img.thumbnail(output_size)
			img.save(self.image1.path)

	@property
	def image2URL(self):
		try:
			url = self.image2.url

		except:
			url = ''
		return url

	def save2(self, *args, **kwargs):
		super(Properties, self).save(*args, **kwargs)

		img = Image.open(self.image2.path)

		if img.height > 360 or img.width > 640:
			output_size = (640, 360)
			img.thumbnail(output_size)
			img.save(self.image2.path)

	@property
	def image3URL(self):
		try:
			url = self.image3.url

		except:
			url = ''
		return url

	def save3(self, *args, **kwargs):
		super(Properties, self).save(*args, **kwargs)

		img = Image.open(self.image3.path)

		if img.height > 360 or img.width > 640:
			output_size = (640, 360)
			img.thumbnail(output_size)
			img.save(self.image3.path)

	@property
	def image4URL(self):
		try:
			url = self.image4.url

		except:
			url = ''
		return url

	def save4(self, *args, **kwargs):
		super(Properties, self).save(*args, **kwargs)

		img = Image.open(self.image4.path)

		if img.height > 360 or img.width > 640:
			output_size = (640, 360)
			img.thumbnail(output_size)
			img.save(self.image4.path)

	@property
	def image5URL(self):
		try:
			url = self.image5.url

		except:
			url = ''
		return url

	def save5(self, *args, **kwargs):
		super(Properties, self).save(*args, **kwargs)

		img = Image.open(self.image5.path)

		if img.height > 360 or img.width > 640:
			output_size = (640, 360)
			img.thumbnail(output_size)
			img.save(self.image5.path)

	@property
	def image6URL(self):
		try:
			url = self.image6.url

		except:
			url = ''
		return url

	def save6(self, *args, **kwargs):
		super(Properties, self).save(*args, **kwargs)

		img = Image.open(self.image6.path)

		if img.height > 360 or img.width > 640:
			output_size = (640, 360)
			img.thumbnail(output_size)
			img.save(self.image6.path)

	@property
	def image7URL(self):
		try:
			url = self.image7.url

		except:
			url = ''
		return url

	def save7(self, *args, **kwargs):
		super(Properties, self).save(*args, **kwargs)

		img = Image.open(self.image7.path)

		if img.height > 360 or img.width > 640:
			output_size = (640, 360)
			img.thumbnail(output_size)
			img.save(self.image7.path)

	@property
	def image8URL(self):
		try:
			url = self.image8.url

		except:
			url = ''
		return url

	def save8(self, *args, **kwargs):
		super(Properties, self).save(*args, **kwargs)

		img = Image.open(self.image8.path)

		if img.height > 360 or img.width > 640:
			output_size = (640, 360)
			img.thumbnail(output_size)
			img.save(self.image8.path)

	@property
	def image9URL(self):
		try:
			url = self.image9.url

		except:
			url = ''
		return url

	def save9(self, *args, **kwargs):
		super(Properties, self).save(*args, **kwargs)

		img = Image.open(self.image9.path)

		if img.height > 360 or img.width > 640:
			output_size = (640, 360)
			img.thumbnail(output_size)
			img.save(self.image9.path)


class Messages(models.Model):
	nom = models.CharField(max_length=20)
	email = models.EmailField(null = True, blank = True)
	mobile = models.CharField(max_length=20)
	sujet = models.CharField(max_length = 100)
	message = models.TextField(blank=True, null=True)
	message_date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return '{}-{}'.format(self.nom, str(self.sujet))