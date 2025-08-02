import markdown
from django.utils.safestring import mark_safe
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail # For sending email notifications
from django.conf import settings # To get email settings
from content_manager.models import (
    BlogPost, Event, PageSection, Program, Cause, TeamMember, Value, Achievement, BannerSlide, Partner,
)
from .forms import ContactForm, FeedbackForm, VolunteerForm
from mail_client.models import FeedbackSubmission, ContactMessage, VolunteerApplication

# Helper function to get PageSection content safely
def get_section(key):
    """Gets the whole PageSection object safely."""
    return PageSection.objects.filter(section_key=key).first()

# --- Main Page Views ---

def home(request):
    # Using filter().first() is safer than get() as it returns None if not found
    banner_title_section = PageSection.objects.filter(section_key='home_banner_title').first()
    banner_text_section = PageSection.objects.filter(section_key='home_banner_text').first()
    about_intro_section = PageSection.objects.filter(section_key='home_about_intro').first()
    
    # home_intro_image section's content field stores the static URL path
    intro_image_section = PageSection.objects.filter(section_key='home_intro_image').first()
    home_tab_about = PageSection.objects.filter(section_key='home_tab_about').first()
    home_tab_vision = PageSection.objects.filter(section_key='home_tab_vision').first()
    home_tab_mission = PageSection.objects.filter(section_key='home_tab_mission').first()
    
    active_slides = BannerSlide.objects.filter(is_active=True).order_by('display_order')
    featured_programs = Program.objects.filter(is_active=True).order_by('display_order')[:3]
    achievements = Achievement.objects.filter(is_active=True).order_by('display_order')
    
    # Partner field
    partners = Partner.objects.filter(is_active=True)

    # Feedback Form Handling (Example integrated here)
    feedback_form = FeedbackForm() # Instantiate for GET request
    if request.method == 'POST' and 'submit_feedback' in request.POST:
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            # --- SAVE FEEDBACK TO MAILBOX ---
            try:
                FeedbackSubmission.objects.create(
                    name=feedback_form.cleaned_data['full_name'],
                    email=feedback_form.cleaned_data['email'],
                    message=feedback_form.cleaned_data['message']
                )
                messages.success(request, "Thank you for your feedback!")
            except Exception as e:
                print(f"Error saving feedback: {e}") # Log error
                messages.error(request, "Sorry, there was an error submitting your feedback.")
            # ----------------------------------
            return redirect('home:home') # Redirect to prevent resubmission
        else:
            messages.error(request, "Please correct the errors in the feedback form.")

    context = {
        'banner_title': banner_title_section.title if banner_title_section else "[Banner Title]",
        'banner_text': banner_title_section.content if banner_title_section else "[Banner Text]",
        'about_intro': about_intro_section.content if about_intro_section else "[About Intro Text]",
        'active_slides': active_slides,
        'intro_image_section': intro_image_section,
        'home_tab_about': home_tab_about,
        'home_tab_vision': home_tab_vision,
        'home_tab_mission': home_tab_mission,
        'featured_programs': featured_programs,
        'achievements': achievements,
        'feedback_form': feedback_form,
        'partners': partners,
    }
    return render(request, 'home/index.html', context)

def about(request):
    mission_section = PageSection.objects.filter(section_key='about_mission').first()
    vision_section = PageSection.objects.filter(section_key='about_vision').first()
    history_section = PageSection.objects.filter(section_key='about_history').first()
    values = Value.objects.filter(is_active=True).order_by('display_order')
    team_members = TeamMember.objects.filter(is_active=True).order_by('display_order')

    context = {
        'mission': mission_section.content if mission_section else "[Mission Statement Missing]",
        'vision': vision_section.content if vision_section else "[Vision Statement Missing]",
        'history': history_section.content if history_section else "[History Text Missing]",
        'values': values,
        'team_members': team_members,
    }
    return render(request, 'home/about.html', context)

def events(request):
    now = timezone.now()
    upcoming_events = Event.objects.filter(
        is_upcoming=True,
        start_datetime__gte=now
    ).order_by('start_datetime')
    past_events = Event.objects.filter(start_datetime__lt=now).order_by('-start_datetime')[:6] # Show some past events
    
    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    }
    return render(request, 'home/events.html', context)

def blog(request):
    # TODO: Add pagination
    blog_posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'home/blog.html', context)

def blog_detail_view(request, slug): # or slug
    post = get_object_or_404(BlogPost, slug=slug)
    post.content = mark_safe(markdown.markdown(post.content, extensions=['fenced_code', 'codehilite', 'extra', 'tables']))
    context = {'post': post}
    return render(request, 'home/blog_detail.html', context)

def contact(request):
    address_section = PageSection.objects.filter(section_key='contact_address').first()
    phone_section = PageSection.objects.filter(section_key='contact_phone').first()
    email_section = PageSection.objects.filter(section_key='contact_email').first()
    map_embed_section = PageSection.objects.filter(section_key='contact_map_embed').first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # --- SAVE CONTACT MESSAGE TO MAILBOX ---
            try:
                ContactMessage.objects.create(
                    name=form.cleaned_data['full_name'],
                    email=form.cleaned_data['email'],
                    subject=form.cleaned_data['subject'],
                    message=form.cleaned_data['message']
                )
                messages.success(request, "Thank you for your message! We will get back to you soon.")
            except Exception as e:
                print(f"Error saving contact message: {e}")
                messages.error(request, "Sorry, there was an error sending your message.")
            # -------------------------------------
            return redirect('home:contact') # Redirect to clear form
        else:
             messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm() # Empty form for GET request

    context = {
        'contact_address': address_section.content if address_section else "[Address Missing]",
        'contact_phone': phone_section.content if phone_section else "[Phone Missing]",
        'contact_email': email_section.content if email_section else "[Email Missing]",
        'map_embed_code': map_embed_section.content if map_embed_section else None,
        'contact_form': form, # Pass form instance to template
    }
    return render(request, 'home/contact.html', context)

def programs(request):
    intro_section = PageSection.objects.filter(section_key='programs_intro').first()
    all_programs = Program.objects.filter(is_active=True).order_by('display_order')
    context = {
        'intro_text': intro_section.content if intro_section else "[Programs Introduction Missing]",
        'programs': all_programs,
    }
    return render(request, 'home/programs.html', context)

def causes(request):
    intro_section = PageSection.objects.filter(section_key='causes_intro').first()
    all_causes = Cause.objects.filter(is_active=True).order_by('display_order')
    context = {
        'intro_text': intro_section.content if intro_section else "[Causes Introduction Missing]",
        'causes': all_causes,
    }
    return render(request, 'home/causes.html', context)

# --- Separate Form Submission Views (Example: Volunteer) ---

def volunteer_application(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
             # --- SAVE VOLUNTEER APP TO MAILBOX ---
            try:
                VolunteerApplication.objects.create(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    gender=form.cleaned_data['gender'],
                    age=form.cleaned_data['age'],
                    contact_number=form.cleaned_data['contact'],
                    email=form.cleaned_data['email'],
                    message=form.cleaned_data['message']
                    # Status defaults to 'Pending'
                )
                messages.success(request, "Thank you for your application! We will be in touch.")
            except Exception as e:
                print(f"Error saving volunteer application: {e}")
                messages.error(request, "Sorry, there was an error submitting your application.")
            # -------------------------------------
        else:
             messages.error(request, "Please correct the errors in the volunteer form.")


    # Redirect back to the page the user came from, or homepage as fallback
    # This prevents direct access via GET and handles completion of POST
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer or '/')


# NOTE: submit_feedback logic was integrated into home view.
# If you want a separate page/view, create it similar to volunteer_application or contact.
def submit_feedback(request):
     messages.info(request, "Feedback submission handled on homepage.")
     return redirect('home:home') # Or redirect to wherever the feedback form lives

# NOTE: submit_contact_form logic was integrated into contact view.
# Keep this separate if preferred, but contact view now handles both GET and POST.
# def submit_contact_form(request):
#     if request.method == 'POST':
#          # ... processing logic ...
#          return redirect('home:contact')
#     else:
#          return redirect('home:contact')