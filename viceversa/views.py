from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['usertext']

	reversed_text = user_text [::-1]

	s = user_text.split()
	l = len(s)
	

	return render(request, 'reverse.html', {'usertext':user_text,
	 'reversedtext':reversed_text,
	 'count':l})