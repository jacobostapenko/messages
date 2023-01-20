from django.shortcuts import render
from django.http import HttpResponse

from . import models


def home(request):
    messages = models.message.objects.all().order_by('-created_at').values()
    context = { 'messages':messages    }
    if request.method == 'POST':
            if request.POST.get('message'):
                post=models.message()
                post.author = request.POST.get('author')
                post.message= request.POST.get('message')
                post.save()
                



    
    return render(request, 'messageboard/home.html', context)




#def createpost(request):
 #       if request.method == 'POST':
 #           if request.POST.get('message'):
 #               post=models.message()
 #              post.message= request.POST.get('message')
  #              post.save()
  #              
  #            #  return home(request)
  #              return render(request, 'messageboard/createpost.html')  
#
  #      else:
  #              return render(request,'messageboard/createpost.html')

