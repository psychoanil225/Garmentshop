from django.shortcuts import render
from garments.models import FormalShirt
from garments.forms import Contactform
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def contactview(request):
    form = Contactform(request.POST or None)
    if form.is_valid():
        subject = 'hello from garmentshop.com'
        message = 'this is what you typed: ' + request.POST.get('content')
        from_email = settings.EMAIL_HOST_USER
        user_email = request.POST.get('contact_email') 
        to_list = [user_email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list, fail_silently=False)
        return HttpResponseRedirect('thankyou')
    return render(request, 'contacthtml.html',{'form':form})
        
       
   
def Shirtsview(request):
    return render(request, 'index.html')
def index(request):
    lst =FormalShirt.objects.all()
    return render(request, 'base.html', {'lst':lst})

def thankyou(request):
    res = HttpResponse()
    res.write('<h1>we just sent a mail to you</h1>')
    res.write('<h1>please go through it</h1>')
    return res