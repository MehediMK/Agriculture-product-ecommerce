from django.urls import path
from user_activity.views import (
    email_subscribe, news_letter, faq_view, about_us_view, terms_conditions, contact)

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('faq-view/', faq_view, name='faq_view'),
    path('news_letter/', news_letter, name='news_letter'),
    path('about-us-view/', about_us_view, name='about_us'),
    path('email-subscribe/', email_subscribe, name='email_subscribe'),
    path('terms-conditions/', terms_conditions, name='terms_conditions'),
]
