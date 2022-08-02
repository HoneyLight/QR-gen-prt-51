
from django.urls import path
from .views import LandingPageView,CONTACTPageView,FAQPageView,ABOUTPageView,DATAPageview,CUSTOMPageview
urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
    path('contact/', CONTACTPageView.as_view(), name='contact-us'),
    path('faq/', FAQPageView.as_view(), name='faq'),
    path('about/', ABOUTPageView.as_view(), name='about'),
    path('datatype/', DATAPageview.as_view(), name='datatype'),
    path('custom/', CUSTOMPageview.as_view(), name='custom'),
    
]
