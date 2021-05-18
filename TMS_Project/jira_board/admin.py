from django.contrib import admin
from .models import Project, ProjectField

# admin.site.register(Project)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('prject_id', 'key', 'name')
    list_filter = ('key', )
    search_fields = ('key', 'name',)


@admin.register(ProjectField)
class ProjectFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'field_id', 'name',)
    list_filter = ('name',)
    search_fields = ('field_id', 'name',)
