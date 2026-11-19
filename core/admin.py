from django.contrib import admin
from .models import SiteSetting, Service, ProjectCategory, Project, Testimonial, QuoteRequest

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'whatsapp', 'email', 'years_experience', 'completed_projects')

    def has_add_permission(self, request):
        # Yalnızca 1 ayar kaydı olsun
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'short_description')


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'completion_year', 'is_featured', 'order')
    list_filter = ('category', 'is_featured', 'completion_year')
    list_editable = ('is_featured', 'order')
    search_fields = ('title', 'location', 'description')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'project_type', 'location', 'rating', 'is_active')
    list_filter = ('rating', 'is_active')
    list_editable = ('is_active',)


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'district', 'service_type', 'created_at', 'is_contacted')
    list_filter = ('service_type', 'is_contacted', 'created_at')
    list_editable = ('is_contacted',)
    search_fields = ('name', 'phone', 'district', 'message')
    readonly_fields = ('created_at',)
