from django.db import models

# Create your models here.
from django_pusher.push import pusher

class Pmessages(models.Model):
	message = models.CharField(max_length=1000)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.message

	def save(self, *args, **kwargs):

		#p['test_channel'].trigger('my_event', {'message': 'hello world'})
		pusher['private-test_channel2'].trigger('my_event', {'message': self.message})

		super(Pmessages, self).save(*args, **kwargs)
