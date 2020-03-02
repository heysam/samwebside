from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext


# def index(request):
#     #return HttpResponse("sam is handsome")
#     render(request,'App/index.html')
# # def detail(request,num,num2):
# #     return HttpResponse("detail-%s-%s" %(num,num2))
def index(request):
    templates = 'App/index.html'
    context={}
    return render(request,templates,context)
