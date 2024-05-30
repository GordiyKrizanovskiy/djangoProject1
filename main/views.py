from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'main/about.html')

def home_page(request):
    return render(request, 'main/home_page.html')