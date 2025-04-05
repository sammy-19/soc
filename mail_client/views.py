from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import ContactMessage, FeedbackSubmission, VolunteerApplication

# --- Mixin for Staff Access ---
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """ Verifies that the user is logged in and is a staff member. """
    login_url = '/accounts/login/' # Or use settings.LOGIN_URL

    def test_func(self):
        return self.request.user.is_staff

# --- Mailbox Dashboard ---
class MailboxDashboardView(StaffRequiredMixin, TemplateView):
    template_name = 'mail_client/mailbox_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unread_message_count'] = ContactMessage.objects.filter(is_read=False).count()
        context['unreviewed_feedback_count'] = FeedbackSubmission.objects.filter(is_reviewed=False).count()
        context['pending_volunteer_count'] = VolunteerApplication.objects.filter(status='Pending').count()
        # Add total counts if desired
        context['total_messages'] = ContactMessage.objects.count()
        context['total_feedback'] = FeedbackSubmission.objects.count()
        context['total_volunteers'] = VolunteerApplication.objects.count()
        return context

# --- Contact Message Views ---
class ContactMessageListView(StaffRequiredMixin, ListView):
    model = ContactMessage
    template_name = 'mail_client/contactmessage_list.html'
    context_object_name = 'messages'
    paginate_by = 20 # Show 20 messages per page
    ordering = ['-received_at'] # Already default in model, but good to be explicit

class ContactMessageDetailView(StaffRequiredMixin, DetailView):
    model = ContactMessage
    template_name = 'mail_client/contactmessage_detail.html'
    context_object_name = 'message'

    # Mark as read when viewed
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.is_read:
            obj.is_read = True
            obj.save(update_fields=['is_read'])
        return obj

# --- Feedback Submission Views ---
class FeedbackListView(StaffRequiredMixin, ListView):
    model = FeedbackSubmission
    template_name = 'mail_client/feedbacksubmission_list.html'
    context_object_name = 'feedbacks'
    paginate_by = 20
    ordering = ['-received_at']

class FeedbackDetailView(StaffRequiredMixin, DetailView):
    model = FeedbackSubmission
    template_name = 'mail_client/feedbacksubmission_detail.html'
    context_object_name = 'feedback'

    # Mark as reviewed when viewed
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.is_reviewed:
            obj.is_reviewed = True
            obj.save(update_fields=['is_reviewed'])
        return obj

# --- Volunteer Application Views ---
class VolunteerApplicationListView(StaffRequiredMixin, ListView):
    model = VolunteerApplication
    template_name = 'mail_client/volunteerapplication_list.html'
    context_object_name = 'applications'
    paginate_by = 20
    ordering = ['-submitted_at']

class VolunteerApplicationDetailView(StaffRequiredMixin, DetailView):
    model = VolunteerApplication
    template_name = 'mail_client/volunteerapplication_detail.html'
    context_object_name = 'application'

    # Add status choices to context for the update form/buttons
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = VolunteerApplication.STATUS_CHOICES
        return context

    # Handle POST request to update status
    def post(self, request, *args, **kwargs):
        application = self.get_object()
        new_status = request.POST.get('status')
        # Validate if the submitted status is valid
        valid_statuses = [choice[0] for choice in VolunteerApplication.STATUS_CHOICES]
        if new_status in valid_statuses:
            application.status = new_status
            application.save(update_fields=['status'])
            messages.success(request, f"Application status updated to '{new_status}'.")
        else:
            messages.error(request, "Invalid status submitted.")
        # Redirect back to the detail page
        return redirect('mail_client:volunteer_detail', pk=application.pk)