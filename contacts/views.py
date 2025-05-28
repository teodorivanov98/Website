from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the message to the database
        Contact.objects.create(name=name, email=email, message=message)

        # Send the message via email
        send_mail(
            subject=f'New contact message from {name}',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],  # Your email address
            fail_silently=False,
        )

        return redirect('contacts-home')  # Or use a success page if you prefer

    # Show past messages below the form
    contacts = Contact.objects.all().order_by('-id')
    return render(request, 'contacts/home.html', {'contacts': contacts})
