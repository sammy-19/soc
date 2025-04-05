from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    received_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-received_at'] # Show newest first
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class FeedbackSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    received_at = models.DateTimeField(default=timezone.now)
    is_reviewed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-received_at']
        verbose_name = "Feedback Submission"
        verbose_name_plural = "Feedback Submissions"

    def __str__(self):
        return f"Feedback from {self.name} ({self.email})"

class VolunteerApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Contacted', 'Contacted'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('prefer_not_to_say', 'Prefer not to say'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.TextField(verbose_name="Reason for Volunteering")
    submitted_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Volunteer Application"
        verbose_name_plural = "Volunteer Applications"

    def __str__(self):
        return f"Application from {self.first_name} {self.last_name}"