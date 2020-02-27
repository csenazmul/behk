from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from .form import *
from .models import *
from django.core.mail import EmailMessage
from django.template.loader import get_template
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def service(request):
    return render(request, 'service.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

# redirect success page
def success(request):
    return render(request, 'success.html')


def contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('contact_form.txt')
            context = {
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'contact_content' : contact_content,
            }
            
            content = template.render(context)

            email = EmailMessage(
                "New contact form email",
                content,
                "Creative web" + '',
                ['pythonbdhouse@gmail.com'],
                headers = { 'Reply To': contact_email }
            )

            email.send()

            return redirect('success')
    return render(request, 'contact.html', {'form':Contact_Form })