# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Type(models.Model):
	name = models.CharField(max_length=20)

	def __unicode__(self):	
		return self.name

class Ebook(models.Model):
	name = models.CharField(max_length=20)
	author = models.CharField(max_length=30)
	brief = models.CharField(max_length=200)
	pub_date = models.DateField('date published') #default=datetime.datetime.now().date()
	types = models.ForeignKey(Type)
	count = models.IntegerField()
	pub_at = models.CharField(max_length=15) 
	
	def __unicode__(self):#中文编码用unicode这个方法
		return self.name

	def was_published_recently(self):
		now = timezone.now()
		return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=3)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
