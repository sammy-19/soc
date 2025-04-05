from django.urls import path
from . import views

app_name = 'mail_client' # Define the namespace

urlpatterns = [
    path('', views.MailboxDashboardView.as_view(), name='dashboard'),

    # Contact Messages
    path('messages/', views.ContactMessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/', views.ContactMessageDetailView.as_view(), name='message_detail'),

    # Feedback Submissions
    path('feedback/', views.FeedbackListView.as_view(), name='feedback_list'),
    path('feedback/<int:pk>/', views.FeedbackDetailView.as_view(), name='feedback_detail'),

    # Volunteer Applications
    path('volunteers/', views.VolunteerApplicationListView.as_view(), name='volunteer_list'),
    path('volunteers/<int:pk>/', views.VolunteerApplicationDetailView.as_view(), name='volunteer_detail'),
    # Note: Status update is handled via POST to the detail view URL
]