from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                done = send_mail(
                    subject="[AD4T][Contact Secretariat] "+ subject,
                    message=message,
                    from_email=email,
                    recipient_list = [('Secretariat AD4T', 'secreteriat@4temps.org')],
                    fail_silently=False
                    )
                if done == 1:
                    # False redirect for now, TODO
                    return HttpResponse('Thanks')
                    #return HttpResponseRedirect("/contact/thanks")
                else:
                    # We could recover the email and send it save the parameters for further analysis
                    return HttpResponse('Error sending email')
                    #return HttpRespnseRedirect("/contact/errorEmailSending")
            except BadHeaderError:
                return HttpResponse('Invalid header found')

    else:
        form = forms.ContactForm()

    return render(request, 'contact.html', locals())
