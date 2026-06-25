from django.contrib import admin
from .models import Experience, ExperienceBullet, Project, ProjectBullet, Skill

class BulletInline(admin.TabularInline):
    model = ExperienceBullet
    extra = 1

class ProjectBulletInline(admin.TabularInline):
    model = ProjectBullet
    extra = 1

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date')
    inlines = [BulletInline]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'severity', 'tech_stack', 'date_range')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectBulletInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'stage', 'order')
    list_filter = ('stage',)
