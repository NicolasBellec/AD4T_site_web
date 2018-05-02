from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

    else:
        form = forms.ContactForm()


    return render(request, 'contact.html', locals())
