from django.shortcuts import render
from django.http import HttpResponse
#Create your views here.
# def main_view(request):
#     return HttpResponse('Learning django')
# def main_view(request):
#     return render(request, 'app_main/index.html')
def main_home(request):
    return render(request, 'app_main/index.html')
def main_about(request):
    return render(request, 'app_main/about_us.html')
def main_contact(request):
    return render(request, 'app_main/contact_us.html')
