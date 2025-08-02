from django import forms
from .models import BlogPost, Event, Partner, PageSection, Program, Cause, TeamMember, Value, Achievement, BannerSlide

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'image', 'content', 'excerpt', 'is_published']
        # You might want to exclude 'author' and set it automatically in the view
        # Or provide a dropdown of users
        widgets = {
            'content': forms.Textarea(attrs={'rows': 15}),
            'excerpt': forms.Textarea(attrs={'rows': 4}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'image', 'start_datetime', 'end_datetime', 'location_name', 'location_address', 'registration_link', 'is_upcoming']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class PageSectionForm(forms.ModelForm):
     class Meta:
        model = PageSection
        fields = ['section_key', 'title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }
        # Make section_key read-only when editing existing sections
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if self.instance and self.instance.pk: # If editing existing instance
                self.fields['section_key'].widget.attrs['readonly'] = True

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'logo', 'website', 'is_active']

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'short_description', 'full_description', 'image', 'key_activities', 'display_order', 'is_active']
        widgets = {
            'full_description': forms.Textarea(attrs={'rows': 10}),
            'key_activities': forms.Textarea(attrs={'rows': 6}),
        }

class CauseForm(forms.ModelForm):
    class Meta:
        model = Cause
        fields = ['title', 'description', 'image', 'goal_description', 'donation_link', 'display_order', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
        }

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'title', 'bio', 'image', 'display_order', 'is_active']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 5}),
        }

class ValueForm(forms.ModelForm):
    class Meta:
        model = Value
        fields = ['name', 'description', 'icon_class', 'display_order', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class AchievementForm(forms.ModelForm):
     class Meta:
        model = Achievement
        fields = ['title', 'description', 'image', 'display_order', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        
class BannerSlideForm(forms.ModelForm):
    class Meta:
        model = BannerSlide
        fields = [
            'title', 'text', 'image', 'button_text',
            'button_link', 'button_action', 'display_order', 'is_active'
        ]
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}), # Adjust rows as needed
        }
        help_texts = { # Optional: Add specific help text here too
            'button_link': "Enter full URL (e.g., https://...) or an anchor (#your-id) or leave '#' for popup actions.",
            'button_action': "Choose 'Open Donate Popup' or 'Open Volunteer Popup' if button_link is '#' and should trigger a popup."
        }