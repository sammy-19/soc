from django.urls import path
from . import views


urlpatterns = [
    path('', views.DashboardView.as_view(), name='cm_dashboard'),

    # Blog Posts
    path('blog/', views.BlogPostListView.as_view(), name='cm_blog_list'),
    path('blog/new/', views.BlogPostCreateView.as_view(), name='cm_blog_new'),
    path('blog/edit/<slug:slug>/', views.BlogPostUpdateView.as_view(), name='cm_blog_edit'), # Use slug for blog
    path('blog/delete/<slug:slug>/', views.BlogPostDeleteView.as_view(), name='cm_blog_delete'),

    # Events
    path('events/', views.EventListView.as_view(), name='cm_event_list'),
    path('events/new/', views.EventCreateView.as_view(), name='cm_event_new'),
    path('events/edit/<int:pk>/', views.EventUpdateView.as_view(), name='cm_event_edit'),
    path('events/delete/<int:pk>/', views.EventDeleteView.as_view(), name='cm_event_delete'),

    # Page Sections (mainly editing and not adding)
    path('sections/', views.PageSectionListView.as_view(), name='cm_section_list'),
    path('sections/edit/<str:pk>/', views.PageSectionUpdateView.as_view(), name='cm_section_edit'), # Use pk (section_key)
    
    # Partner
    path('partners/', views.partner_list, name='cm_partner_list'),
    path('partners/add/', views.partner_form, name='cm_partner_add'),
    path('partners/<int:pk>/edit/', views.partner_form, name='cm_partner_edit'),
    path('partners/<int:pk>/delete/', views.partner_delete, name='cm_partner_delete'),

    # Programs
    path('programs/', views.ProgramListView.as_view(), name='cm_program_list'),
    path('programs/new/', views.ProgramCreateView.as_view(), name='cm_program_new'),
    path('programs/edit/<int:pk>/', views.ProgramUpdateView.as_view(), name='cm_program_edit'),
    path('programs/delete/<int:pk>/', views.ProgramDeleteView.as_view(), name='cm_program_delete'),

    # Causes
    path('causes/', views.CauseListView.as_view(), name='cm_cause_list'),
    path('causes/new/', views.CauseCreateView.as_view(), name='cm_cause_new'),
    path('causes/edit/<int:pk>/', views.CauseUpdateView.as_view(), name='cm_cause_edit'),
    path('causes/delete/<int:pk>/', views.CauseDeleteView.as_view(), name='cm_cause_delete'),

    # Team Members
    path('team/', views.TeamMemberListView.as_view(), name='cm_teammember_list'),
    path('team/new/', views.TeamMemberCreateView.as_view(), name='cm_teammember_new'),
    path('team/edit/<int:pk>/', views.TeamMemberUpdateView.as_view(), name='cm_teammember_edit'),
    path('team/delete/<int:pk>/', views.TeamMemberDeleteView.as_view(), name='cm_teammember_delete'),

    # Values
    path('values/', views.ValueListView.as_view(), name='cm_value_list'),
    path('values/new/', views.ValueCreateView.as_view(), name='cm_value_new'),
    path('values/edit/<int:pk>/', views.ValueUpdateView.as_view(), name='cm_value_edit'),
    path('values/delete/<int:pk>/', views.ValueDeleteView.as_view(), name='cm_value_delete'),

    # Achievements
    path('achievements/', views.AchievementListView.as_view(), name='cm_achievement_list'),
    path('achievements/new/', views.AchievementCreateView.as_view(), name='cm_achievement_new'),
    path('achievements/edit/<int:pk>/', views.AchievementUpdateView.as_view(), name='cm_achievement_edit'),
    path('achievements/delete/<int:pk>/', views.AchievementDeleteView.as_view(), name='cm_achievement_delete'),
    
     # Banner Slides
    path('banners/', views.BannerSlideListView.as_view(), name='cm_bannerslide_list'),
    path('banners/new/', views.BannerSlideCreateView.as_view(), name='cm_bannerslide_new'),
    path('banners/edit/<int:pk>/', views.BannerSlideUpdateView.as_view(), name='cm_bannerslide_edit'),
    path('banners/delete/<int:pk>/', views.BannerSlideDeleteView.as_view(), name='cm_bannerslide_delete'),
]
