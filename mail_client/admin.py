from django.contrib import admin
from .models import ContactMessage, FeedbackSubmission, VolunteerApplication

# Register your models here.

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'received_at', 'is_read')
    list_filter = ('is_read', 'received_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('is_read',) # Allows changing read status in list view
    readonly_fields = ('name', 'email', 'subject', 'message', 'received_at') # Make fields read-only in detail view

    # Prevent adding contact messages via admin
    def has_add_permission(self, request):
        return False

@admin.register(FeedbackSubmission)
class FeedbackSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'received_at', 'is_reviewed')
    list_filter = ('is_reviewed', 'received_at')
    search_fields = ('name', 'email', 'message')
    list_editable = ('is_reviewed',)
    readonly_fields = ('name', 'email', 'message', 'received_at')

    def has_add_permission(self, request):
        return False

@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'contact_number', 'submitted_at', 'status')
    list_filter = ('status', 'submitted_at', 'gender')
    search_fields = ('first_name', 'last_name', 'email', 'contact_number', 'message')
    list_editable = ('status',) # Allow changing status in list view
    readonly_fields = (
        'first_name', 'last_name', 'gender', 'age',
        'contact_number', 'email', 'message', 'submitted_at'
    )

    def has_add_permission(self, request):
        return False