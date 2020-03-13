from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

###################### RELATIONSHIP OBJECTS ############################

class Relation(models.Model):
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	'''def __str__(self):
		return str(str(self.content_type) + " > " +str( "" ) )'''

class Relationship(models.Model):

	IS_RELATED_TO = 0
	WORKS_ON = 1
	COMMISSIONS = 2   
	WORKS_FOR = 3
	EMPLOYS = 4

	RELATIONSHIPS = (
		(IS_RELATED_TO, 'Is related to'),
		(WORKS_ON, 'Works on'),
		(COMMISSIONS, 'Commissioned'),
		(WORKS_FOR, 'Works for'),
		(EMPLOYS, 'Employs'),
   )
	kind = models.PositiveSmallIntegerField(choices=RELATIONSHIPS,default=IS_RELATED_TO)

	reverse_name = models.CharField(max_length=30, null=True, default='', blank=True)
	bidirectional = models.BooleanField(null=False, default=True)

	otherobject = GenericRelation(Relation,)

	def __str__(self):

		return str(self.otherobject.name)


########################### CONTENT OBJECTS ############################

class Person(models.Model):
	title = models.CharField(max_length=30, null=True, default='')
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	url = models.URLField(max_length=250, null=True, default='', blank=True)
	about = models.TextField(default='', null=True, blank=True)
	related_to = models.ManyToManyField(Relationship, blank=True)

	def __str__(self):
		return self.first_name + " "  + self.last_name


class Funder(models.Model):
	name = models.CharField(max_length=200, null=True, default='')
	text = models.TextField(null=True, default='', blank=True)
	related_to = models.ManyToManyField(Relationship, blank=True)
	def __str__(self):
		return self.name
	 

class ResearchCategory(models.Model):
	name = models.CharField(max_length=200, null=True, default='')
	text = models.TextField(null=True, default='', blank=True)
	related_to = models.ManyToManyField(Relationship, blank=True)
	def __str__(self):
		return self.name
	

class ResearchArea(models.Model):
	name = models.CharField(max_length=200, null=True, default='')
	category = models.ForeignKey(ResearchCategory, on_delete=models.CASCADE, null=True, default=None, blank=True)
	text = models.TextField(null=True, default='', blank=True)
	related_to = models.ManyToManyField(Relationship, blank=True)
	def __str__(self):
		return self.name
	

class Organisation(models.Model):
	name = models.CharField(max_length=200)
	url = models.URLField(max_length=250, null=True, default='', blank=True)	
	text = models.TextField(null=True, default='', blank=True)
	related_to = models.ManyToManyField(Relationship, blank=True)
	def __str__(self):
		return self.name

	
class ResearchProject(models.Model):
	owner = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, default=None, related_name="owner", blank=True)

	name = models.CharField(max_length=200)
	url = models.URLField(max_length=250, null=True, default='', blank=True)
	text = models.TextField(null=True, default='', blank=True)

	start_date = models.DateField(null=True,  default=None, blank=True)
	end_date = models.DateField(null=True,  default=None, blank=True)
	euros = models.IntegerField(null=True, default=0, blank=True)
	related_to = models.ManyToManyField(Relationship, blank=True)

	def __str__(self):
		return self.name