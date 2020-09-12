from django.db import models

class Data(models.Model):
	pod = models.CharField(max_length=20)
	pwt = models.CharField(max_length=20)
	pd = models.CharField(max_length=20)
	ca = models.CharField(max_length=20)
	fbet = models.CharField(max_length=20)
	fbed = models.CharField(max_length=20)
	ad = models.CharField(max_length=20)
	wd = models.CharField(max_length=20)
	swd = models.CharField(max_length=20)

