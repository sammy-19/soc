from django.contrib import admin
from .models import BlogPost, Event, PageSection, Program, Cause, TeamMember, Value, Achievement, BannerSlide

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_published')
    list_filter = ('is_published', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)} # Auto-populate slug

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_datetime', 'location_name', 'is_upcoming')
    list_filter = ('is_upcoming',)
    search_fields = ('title', 'description', 'location_name')

@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ('section_key', 'title', 'updated_at')
    search_fields = ('section_key', 'title', 'content')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    ordering = ('display_order',)

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    ordering = ('display_order',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'title')
    ordering = ('display_order',)

@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    ordering = ('display_order',)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    ordering = ('display_order',)
    
@admin.register(BannerSlide)
class BannerSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'is_active') # Fields to show in the list view
    list_filter = ('is_active',) # Allow filtering by active status
    search_fields = ('title', 'text') # Allow searching by title and text
    list_editable = ('display_order', 'is_active') # Allow editing order/status directly in the list
    ordering = ('display_order',) 