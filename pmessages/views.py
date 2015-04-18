from django.shortcuts import render
from .models import Pmessages
# Create your views here.

def home(request):
	pmessages = Pmessages.objects.all()
	context = {'pmessages': pmessages}
	print "ha"
	return render(request, 'pmessages/index.html', context)
