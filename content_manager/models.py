from django.db import models
from django.db import models
from django.contrib.auth.models import User # If you want to track authors
from django.utils.text import slugify
from django.urls import reverse
from cloudinary.models import CloudinaryField


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True) # Unique slug for URLs
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image = CloudinaryField('image', folder='blog_images/', null=True, blank=True) # Requires Pillow
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True, help_text="Short summary for blog listing page.")
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('blog_detail', kwargs={'pk': self.pk})
        # If you prefer slugs:
        return reverse('home:blog_detail', kwargs={'slug': self.slug})

# Model for Events
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', folder='event_images/', null=True, blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True)
    location_name = models.CharField(max_length=150)
    location_address = models.CharField(max_length=255, blank=True)
    registration_link = models.URLField(blank=True)
    is_upcoming = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Generic model for simple text sections on pages
class PageSection(models.Model):
    # Use a unique key to identify which section this is
    # e.g., 'about_mission', 'about_vision', 'home_banner_title'
    section_key = models.CharField(max_length=100, unique=True, primary_key=True)
    title = models.CharField(max_length=200, blank=True) # Optional title for the section
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.section_key
    
# Models for Partner
class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='partners/')
    website = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Program, Cause, TeamMember, Value, Achievement etc.

class Program(models.Model):
    name = models.CharField(max_length=150)
    short_description = models.CharField(max_length=250, blank=True, help_text="Brief description for summaries.")
    full_description = models.TextField()
    image = CloudinaryField('image', folder='program_images/', null=True, blank=True)
    key_activities = models.TextField(blank=True, help_text="List key activities, perhaps one per line.")
    display_order = models.PositiveIntegerField(default=0, help_text="Order on the programs page (lower numbers first).")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return self.name

class Cause(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', folder='cause_images/', null=True, blank=True)
    goal_description = models.CharField(max_length=100, blank=True, help_text="Optional: e.g., 'Fundraising Target: $5,000'")
    donation_link = models.URLField(blank=True, help_text="Link to specific donation page for this cause, if any.")
    display_order = models.PositiveIntegerField(default=0, help_text="Order on the causes page.")
    is_active = models.BooleanField(default=True) # Show this cause on the frontend?

    class Meta:
        ordering = ['display_order', 'title']

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = CloudinaryField('image', folder='team_images/', null=True, blank=True)
    display_order = models.PositiveIntegerField(default=0, help_text="Order on the about page.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return self.name

class Value(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, blank=True, help_text="e.g., 'fa fa-handshake-o'. Requires Font Awesome.")
    display_order = models.PositiveIntegerField(default=0, help_text="Order on the about page.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return self.name

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = CloudinaryField('image', folder='achievement_images/', null=True, blank=True)
    display_order = models.PositiveIntegerField(default=0, help_text="Order on the homepage/achievements section.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'title']

    def __str__(self):
        return self.title


class BannerSlide(models.Model):
    ACTION_CHOICES = [
        ('link', 'Link'),
        ('donate', 'Open Donate Popup'),
        ('volunteer', 'Open Volunteer Popup'),
        # Add more actions if needed
    ]

    title = models.CharField(max_length=150)
    text = models.TextField(max_length=300, blank=True)
    image = CloudinaryField('image', folder='images/banner_images/', help_text="Recommended size: e.g., 1920x800 pixels")
    button_text = models.CharField(max_length=50, blank=True, default="Learn More") # More generic default
    button_link = models.CharField(max_length=255, blank=True, default="#", help_text="URL (#anchor, page URL) or leave '#' for popup actions")
    button_action = models.CharField(max_length=20, choices=ACTION_CHOICES, default='link', help_text="What should the button do?")
    display_order = models.PositiveIntegerField(default=0, help_text="Order of appearance (lower numbers first).")
    is_active = models.BooleanField(default=True, help_text="Show this slide on the website.")

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title