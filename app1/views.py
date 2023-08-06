from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *

# Create your views here.
def first(request):
         if request.method =='POST':
         
            username=request.POST['un']
            password=request.POST['pw']
            print(username)
            print(password)
            return HttpResponse(' data submitted')
         return render(request,'first.html')




def inserttopic(request):
      if request.method=='POST':
            topic=request.POST['topic']
            TO=Topic.objects.get_or_create(topic_name=topic)[0]
            TO.save()
            return HttpResponse('insertion is done')
                                                            
      return render(request,'inserttopic.html')
              