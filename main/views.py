from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from contacts.models import Contact

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save message
        Contact.objects.create(name=name, email=email, message=message)

        # Send email
        send_mail(
            subject=f'New contact message from {name}',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return redirect('home')

    return render(request, 'main/home.html')
