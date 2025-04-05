from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # For permissions
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import BlogPost, Event, PageSection, Program, Cause, TeamMember, Value, Achievement, BannerSlide
from .forms import BlogPostForm, EventForm, PageSectionForm, ProgramForm, CauseForm, TeamMemberForm, ValueForm, AchievementForm, BannerSlideForm


# Mixin to check for staff status (or define custom groups/permissions)
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

# --- Dashboard ---
class DashboardView(StaffRequiredMixin, TemplateView):
    template_name = 'content_manager/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_post_count'] = BlogPost.objects.count()
        context['event_count'] = Event.objects.count()
        context['section_count'] = PageSection.objects.count()
        context['program_count'] = Program.objects.count()
        context['cause_count'] = Cause.objects.count()
        context['team_member_count'] = TeamMember.objects.count()
        context['value_count'] = Value.objects.count()
        context['achievement_count'] = Achievement.objects.count()
        return context

# --- Blog Post Management ---
class BlogPostListView(StaffRequiredMixin, ListView):
    model = BlogPost
    template_name = 'content_manager/blogpost_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class BlogPostCreateView(StaffRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'content_manager/blogpost_form.html'
    success_url = reverse_lazy('cm_blog_list') # Redirect to list after creation

    # Optional: Set author automatically
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

class BlogPostUpdateView(StaffRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'content_manager/blogpost_form.html'
    success_url = reverse_lazy('cm_blog_list')

class BlogPostDeleteView(StaffRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'content_manager/confirm_delete.html' # Generic confirmation template
    success_url = reverse_lazy('cm_blog_list')


# --- Event Management ---
class EventListView(StaffRequiredMixin, ListView):
    model = Event
    template_name = 'content_manager/event_list.html'
    context_object_name = 'events'
    ordering = ['-start_datetime']

class EventCreateView(StaffRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'content_manager/event_form.html'
    success_url = reverse_lazy('cm_event_list')

class EventUpdateView(StaffRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'content_manager/event_form.html'
    success_url = reverse_lazy('cm_event_list')

class EventDeleteView(StaffRequiredMixin, DeleteView):
    model = Event
    template_name = 'content_manager/confirm_delete.html'
    success_url = reverse_lazy('cm_event_list')

# --- Page Section Management ---
class PageSectionListView(StaffRequiredMixin, ListView):
    model = PageSection
    template_name = 'content_manager/pagesection_list.html'
    context_object_name = 'sections'
    ordering = ['section_key']

# Editing makes more sense here.
class PageSectionUpdateView(StaffRequiredMixin, UpdateView):
    model = PageSection
    form_class = PageSectionForm
    template_name = 'content_manager/pagesection_form.html'
    success_url = reverse_lazy('cm_section_list')
    # PK URL conf uses 'pk', which maps to section_key because it's the primary key

# --- Program Management ---
class ProgramListView(StaffRequiredMixin, ListView):
    model = Program
    template_name = 'content_manager/program_list.html'
    context_object_name = 'programs'
    ordering = ['display_order', 'name']

class ProgramCreateView(StaffRequiredMixin, CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'content_manager/program_form.html'
    success_url = reverse_lazy('cm_program_list')

class ProgramUpdateView(StaffRequiredMixin, UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'content_manager/program_form.html'
    success_url = reverse_lazy('cm_program_list')

class ProgramDeleteView(StaffRequiredMixin, DeleteView):
    model = Program
    template_name = 'content_manager/confirm_delete.html'
    success_url = reverse_lazy('cm_program_list')

# --- Cause Management ---
class CauseListView(StaffRequiredMixin, ListView):
    model = Cause
    template_name = 'content_manager/cause_list.html'
    context_object_name = 'causes'
    ordering = ['display_order', 'title']

class CauseCreateView(StaffRequiredMixin, CreateView):
    model = Cause
    form_class = CauseForm
    template_name = 'content_manager/cause_form.html'
    success_url = reverse_lazy('cm_cause_list')

class CauseUpdateView(StaffRequiredMixin, UpdateView):
    model = Cause
    form_class = CauseForm
    template_name = 'content_manager/cause_form.html'
    success_url = reverse_lazy('cm_cause_list')

class CauseDeleteView(StaffRequiredMixin, DeleteView):
    model = Cause
    template_name = 'content_manager/confirm_delete.html'
    success_url = reverse_lazy('cm_cause_list')

# --- Team Member Management ---
class TeamMemberListView(StaffRequiredMixin, ListView):
    model = TeamMember
    template_name = 'content_manager/teammember_list.html'
    context_object_name = 'team_members'
    ordering = ['display_order', 'name']

class TeamMemberCreateView(StaffRequiredMixin, CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'content_manager/teammember_form.html'
    success_url = reverse_lazy('cm_teammember_list')

class TeamMemberUpdateView(StaffRequiredMixin, UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'content_manager/teammember_form.html'
    success_url = reverse_lazy('cm_teammember_list')

class TeamMemberDeleteView(StaffRequiredMixin, DeleteView):
    model = TeamMember
    template_name = 'content_manager/confirm_delete.html'
    success_url = reverse_lazy('cm_teammember_list')

# --- Value Management ---
class ValueListView(StaffRequiredMixin, ListView):
    model = Value
    template_name = 'content_manager/value_list.html'
    context_object_name = 'values'
    ordering = ['display_order', 'name']

class ValueCreateView(StaffRequiredMixin, CreateView):
    model = Value
    form_class = ValueForm
    template_name = 'content_manager/value_form.html'
    success_url = reverse_lazy('cm_value_list')

class ValueUpdateView(StaffRequiredMixin, UpdateView):
    model = Value
    form_class = ValueForm
    template_name = 'content_manager/value_form.html'
    success_url = reverse_lazy('cm_value_list')

class ValueDeleteView(StaffRequiredMixin, DeleteView):
    model = Value
    template_name = 'content_manager/confirm_delete.html'
    success_url = reverse_lazy('cm_value_list')

# --- Achievement Management ---
class AchievementListView(StaffRequiredMixin, ListView):
    model = Achievement
    template_name = 'content_manager/achievement_list.html'
    context_object_name = 'achievements'
    ordering = ['display_order', 'title']

class AchievementCreateView(StaffRequiredMixin, CreateView):
    model = Achievement
    form_class = AchievementForm
    template_name = 'content_manager/achievement_form.html'
    success_url = reverse_lazy('cm_achievement_list')

class AchievementUpdateView(StaffRequiredMixin, UpdateView):
    model = Achievement
    form_class = AchievementForm
    template_name = 'content_manager/achievement_form.html'
    success_url = reverse_lazy('cm_achievement_list')

class AchievementDeleteView(StaffRequiredMixin, DeleteView):
    model = Achievement
    template_name = 'content_manager/confirm_delete.html'
    success_url = reverse_lazy('cm_achievement_list')
    
# --- Banner Slide Management ---
class BannerSlideListView(StaffRequiredMixin, ListView):
    model = BannerSlide
    template_name = 'content_manager/bannerslide_list.html' # Template we will create
    context_object_name = 'slides'
    ordering = ['display_order']

class BannerSlideCreateView(StaffRequiredMixin, CreateView):
    model = BannerSlide
    form_class = BannerSlideForm
    template_name = 'content_manager/bannerslide_form.html' # Template we will create
    success_url = reverse_lazy('cm_bannerslide_list')

class BannerSlideUpdateView(StaffRequiredMixin, UpdateView):
    model = BannerSlide
    form_class = BannerSlideForm
    template_name = 'content_manager/bannerslide_form.html'
    success_url = reverse_lazy('cm_bannerslide_list')

class BannerSlideDeleteView(StaffRequiredMixin, DeleteView):
    model = BannerSlide
    template_name = 'content_manager/confirm_delete.html' # Reuse generic confirm delete
    success_url = reverse_lazy('cm_bannerslide_list')