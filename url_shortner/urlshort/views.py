from django.shortcuts import render
from .models import ShortURL
from .forms import createNewShortURL
import random, string


# Create your views here.


def home(request):
     return render(request, 'base.html')





def createShortURL(request):
     if request.method =="POST":
          form = createNewShortURL(request.POST)
          if form.is_valid():
           org_website = form.cleaned_data['long_url']
           random_chars_list = list(string.ascii_letters)
           random_chars =''
           for i in range(10):
               random_chars+= random.choice(random_chars_list)
           while len(ShortURL.objects.filter(short_url=random_chars)) >0:
               random_chars =''
               for i in range(10):
                    random_chars+= random.choice(random_chars_list)
           object = ShortURL(long_url = org_website, short_url= random_chars)
           object.save()   
           url = random_chars
           current_obj = ShortURL.objects.filter(short_url = url)
           if len(current_obj)==0:
               return render(request, 'pagenotfound.html')
           context = { 'obj': current_obj[0]}
           return render(request, 'redirect.html', context)
           #context = {'chars' : random_chars}
           #return render(request, 'urlcreated.html', context) 
     else:
          form = createNewShortURL()
          context ={'form': form}
          return render(request, 'create.html', context)



def list_all_urls(request):
    url_list = ShortURL.objects.all()
    context = {"url_list": url_list}
    return render(request, 'view_list.html', context)
    