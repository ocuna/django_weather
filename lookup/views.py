from django.shortcuts import render

# we need to pass this request
def home(request):
	# render is imported and needs certain arguments
	return render(request, 'home.html', {})


# we need to pass this request
def about(request):
	# render is imported and needs certain arguments
	return render(request, 'about.html', {})
