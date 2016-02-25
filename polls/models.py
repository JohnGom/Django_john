import datetime
from django.utils import timezone


from django.db import models


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def was_publisher_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def __unicode__(self):
		return self.question_text


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_tex = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_tex