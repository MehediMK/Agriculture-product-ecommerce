from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from user_activity.models import (
    EmailSubscription, Newsletter, FAQ, TermsCondition, ContactUs)


def email_subscribe(request):
    if request.method == 'POST':
        if email := request.POST.get('email'):
            EmailSubscription(email=email).save()
    return redirect('index')


def news_letter(request):
    if request.method == 'POST':
        if email := request.POST.get('email'):
            if name := request.POST.get('email'):
                Newsletter(name=name, email=email).save()
    return redirect('index')


def faq_view(request):
    context = {}
    faq_list = FAQ.objects.filter(status=True)
    context.update({'faqs': faq_list})

    return render(request, 'common/faq.html', context)


def about_us_view(request):
    context = {}

    return render(request, 'common/about_us.html', context)


def terms_conditions(request):
    context = {}
    term_list = TermsCondition.objects.filter(status=True)
    context.update({'terms': term_list})
    return render(request, 'common/terms.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and subject and message:
            ContactUs(name=name, email=email,
                      subject=subject, message=message).save()
            try:
                from_email = settings.DEFAULT_FROM_EMAIL
                send_mail(subject, message, from_email, [
                          email],  fail_silently=False,)
                messages.success(
                    request, f"Hello {name},\nThanks for contact with us!")
            except BadHeaderError as error:
                messages.error(request, f"{error}")
        else:
            messages.error(
                request, f"Mail Subject or message body or your email error")

    return render(request, 'shop/contact.html')
