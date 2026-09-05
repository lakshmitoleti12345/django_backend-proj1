from django.shortcuts import render

# Create your views here.
def pages(req):
  return render(req,'satya.html')
