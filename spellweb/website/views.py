from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Work, Blog
from .forms import Blogform, Messageform, WorkForm
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from .models import Apply, Media
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        return render(request, 'contact.html', {'name': name})

        send_mail(
            name,
            subject,
            message,
            email,
            ['diwas.biswakarma1@gmail.com'],
        )
    else:
        return render(request, 'contact.html')


def apply(request):
    return render(request, 'form.html', {})
    """
    if request.method == "GET":
        form = WorkForm()
        return render(request, 'form.html', {'form': form})
    elif request.method == "POST":
        form = WorkForm(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        address = request.POST['address']
        city = request.POST['city']
        age = request.POST['age']
        gender = request.POST['gender']
        message = request.POST['message']
        cv = request.POST['cv']
        form.save()
        return HttpResponseRedirect('/home')
    """


def new_apply(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        address = request.POST['address']
        city = request.POST['city']
        age = request.POST['age']
        gender = request.POST['gender']
        letter = request.POST['letter']
        cv = request.POST['cv']

        object_ref = Work(name=name, email=email, subject=subject, address=address, city=city, age=age, gender=gender,  letter=letter, cv=cv)
        object_ref.save()
        return render(request, 'form.html', {'name': name})


def success(request):
    return HttpResponse("Your Application has been Submitted")


def info(request):
    item = Blog.objects.all
    return render(request, 'info.html', {'item': item})


def media(request):
    all_media = Media.objects.all
    return render(request, 'media.html', {'page': all_media})

#def page_not_found(request):
 #   response = render_to_response('404.html',context_instance=RequestContext(request))
  #  response.status_code = 404

    #return response


def career(request):
    all_career = Apply.objects.all
    return render(request, 'career.html', {'car': all_career})

