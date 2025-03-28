from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name="home"),
    path('feedback/', views.submit_feedback, name="submit_feedback"),
    path('apply/', views.volunteer_application, name="volunteer_application"),
    path('about/', views.about, name="about"),
    path('events/', views.events, name="events"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('programs/', views.programs, name="programs"),
    path('causes/', views.causes, name="causes"),
]